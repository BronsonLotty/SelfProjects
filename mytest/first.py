if __name__ == "__main__":
    Parent ="absdefgh"
    Child = "asdf"
    result = "Yes"
    oldindex = -1
    n = 0
    if Child == '':
        print(result)
    else:
        for i in Child:
            n+=1
            if i in Parent:
                if n == len(Child):
                    result = "Yes"
                    break
                else:
                    try:
                        print(Parent.index[i])
                        Parent = Parent[Parent.index[i]+1:]
                    except:
                        result = "No"
                        break
            else:
                result = "No"
                break
        print(result)