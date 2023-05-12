paths_to_check =  ['C:/Users/altji/Pictures','C:/Users/altji/Documents/Guild Wars 2','C:/Users/altji/Pictures/toto','C:/Users/altji/Pictures/pingouin']



for  indexX in range(0, len(paths_to_check)-1) :
    print(f"checking {paths_to_check[indexX]}")
    for indexY in range(indexX+1, len(paths_to_check)) :
            print(f"checking {paths_to_check[indexX]} and {paths_to_check[indexY]}")
            indexY=+1

    indexX=indexX+1
