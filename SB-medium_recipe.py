# Let's practice writing functions with something useful that needs to calculated often

def sb_medium(liters: int):
    p = liters * 30
    y = liters * 20
    m = liters * 10
    n = liters * 0.7

    print("Recipe for",liters, "L of SB-medium\n"
    "\n"
    "Peptone/Tryptone:",p,"g\n"
    "Yeast extract:",y,"g\n"
    "MOPS:",m,"g\n"
    "NaOH:",n,"g\n"
    "Fill to",0.9*liters*1000,"mL mQ-H2O.\n"
    "Adjust pH to 7.0 with NaOH or HCl.\n"
    "Fill to",liters,"L.\n"
    "Sterilize by autoclaving.")


sb_medium(4)
