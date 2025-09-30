from collections import defaultdict, deque


class SmartRegisterAllocator:
    def __init__(self, regs=("R1", "R2", "R3")):
        self.regs = list(regs)
        self.bind = {r: None for r in self.regs}
        self.where = {}
        self.mem = {}
        self.mem_id = 0

    def build_next_use(self, tac):
        uses = defaultdict(deque)
        for i, instr in enumerate(tac):
            op = instr[0]
            if op in ("add", "sub", "mul", "div"):
                _, dst, x, y = instr
                for v in (x, y):
                    if isinstance(v, str):
                        uses[v].append(i)
            elif op == "mov":
                _, dst, x = instr
                if isinstance(x, str):
                    uses[x].append(i)
            elif op == "imm":
                pass

        next_use = [defaultdict(lambda: None) for _ in range(len(tac))]
        last_seen = {v: None for v in uses}
        for v, q in uses.items():
            for idx in q:
                pass
        future = defaultdict(lambda: None)
        for i in range(len(tac) - 1, -1, -1):
            op = tac[i][0]
            # copia estado actual
            for v, nxt in list(future.items()):
                next_use[i][v] = nxt
            if op in ("add", "sub", "mul", "div"):
                _, dst, x, y = tac[i]
                future[x] = next_use[i].get(x, None)
                future[y] = next_use[i].get(y, None)
                future[dst] = None
            elif op == "mov":
                _, dst, x = tac[i]
                future[x] = next_use[i].get(x, None)
                future[dst] = None
            elif op == "imm":
                _, dst, _ = tac[i]
                future[dst] = None
        return next_use

    def get_reg(self, var, i, next_use):
        for r, v in self.bind.items():
            if v == var:
                self.where[var] = ("reg", r)
                return r
        for r in self.regs:
            if self.bind[r] is None:
                self.bind[r] = var
                self.where[var] = ("reg", r)
                return r
        victim_reg, victim_var, best_score = None, None, -1
        for r, v in self.bind.items():
            nxt = next_use[i].get(v, None)
            score = 10**9 if nxt is None else nxt
            if score > best_score:
                best_score = score
                victim_reg, victim_var = r, v
        slot = f"mem{self.mem_id}"
        self.mem_id += 1
        self.mem[slot] = victim_var
        self.where[victim_var] = ("mem", slot)
        self.bind[victim_reg] = var
        self.where[var] = ("reg", victim_reg)
        return victim_reg
