import os

data_folder = "./transformer data"

os.system("sacrebleu -t wmt13 -l en-de --echo src > '" + os.path.join(data_folder, "val.en") + "'")
os.system("sacrebleu -t wmt13 -l en-de --echo ref > '" + os.path.join(data_folder, "val.de") + "'")
print("\n")
os.system("sacrebleu -t wmt14/full -l en-de --echo src > '" + os.path.join(data_folder, "test.en") + "'")
os.system("sacrebleu -t wmt14/full -l en-de --echo ref > '" + os.path.join(data_folder, "test.de") + "'")