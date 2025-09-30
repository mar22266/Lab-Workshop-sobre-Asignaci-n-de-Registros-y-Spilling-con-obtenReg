class RegisterAllocator:
    def __init__(self, regs=("R1", "R2", "R3")):
        self.registers = {r: None for r in regs}
        self.location = {}
        self.memory = {}
        self.next_spill = 0

    def get_register(self, var):
        for r, v in self.registers.items():
            if v == var:
                self.location[var] = f"reg:{r}"
                return r
        for r in self.registers:
            if self.registers[r] is None:
                self.registers[r] = var
                self.location[var] = f"reg:{r}"
                return r
        return self.spill_and_assign(var)

    def spill_and_assign(self, var):
        spill_reg = next(iter(self.registers.keys()))
        spilled_var = self.registers[spill_reg]
        mem_slot = f"mem{self.next_spill}"
        self.memory[mem_slot] = spilled_var
        self.location[spilled_var] = f"mem:{mem_slot}"
        self.next_spill += 1
        self.registers[spill_reg] = var
        self.location[var] = f"reg:{spill_reg}"
        return spill_reg

    def __str__(self):
        return f"REGISTERS={self.registers}\nMEMORY={self.memory}\nLOCATION={self.location}"
