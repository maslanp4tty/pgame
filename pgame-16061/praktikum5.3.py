dc = {"Kampus":"UMMU", "Prodi":"Info","Lokasi":"Ternate","Tahun":2019}
print(dc["Tahun"])
print(dc.get("Tahun"))

dc["Tahun"]=2020
dc["Lokasi"]="sasa"

print("Directory :", dc)