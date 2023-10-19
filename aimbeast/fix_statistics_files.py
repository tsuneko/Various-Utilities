import os, json, codecs

bom = codecs.BOM_UTF16_LE

def read_json_utf16le(fp):
    with open(fp, 'rb') as f:
        return json.loads(f.read()[len(bom):].decode('utf-16le'))

scenarios = os.listdir()
for file in scenarios:
    scen = file[:-5]
    if scen + " .json" in scenarios:
        # read statistics from both files
        data1 = read_json_utf16le(scen + " .json")
        data2 = read_json_utf16le(scen + ".json")

        # merge statistics
        for key in data1.keys():
            data1[key] += data2[key]

        # delete original stats file
        os.remove(scen + " .json")

        # overwrite new stats file
        with open(scen + ".json", "wb") as f:
            f.write(bom)
            f.write(json.dumps(data1).encode('utf-16le'))

        print(f"Fixed {scen}")

print("Done")
