import pandas as pd

pokemon=pd.read_csv("pokemon_data.csv")

poke_HP=pokemon.sort_values (["HP"], ascending=False).reset_index(drop=True)
poke_ATK=pokemon.sort_values (["Attack"], ascending=False).reset_index (drop=True)

poke1=poke_HP.loc[[0]]
poke2=poke_HP.loc[[1]]
poke3=poke_HP.loc[[0]]
poke4=poke_HP.loc[[1]]
poke5=poke_HP.loc[[0]]
poke6=poke_HP.loc[[1]]

poke_final=pd.concat ([poke1,poke2,poke3,poke4, poke6]).reset_index(drop=True)
print (poke_final)

poke_final.to_csv("time_1.csv", index=False)
