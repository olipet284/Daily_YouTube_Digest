import pandas as pd

df = pd.read_csv("abonnementer.csv")

name_id_list = zip(df['Kanalnavn'],df['Kanal-id'])
name_id_list = sorted(name_id_list)


print('channels = [')
for i, (channel_name, channel_id) in enumerate(name_id_list):
  if i == len(name_id_list) - 1:
    print(f'    "{channel_id}"  # {channel_name}')
  else:
    print(f'    "{channel_id}", # {channel_name}')
print(']')
