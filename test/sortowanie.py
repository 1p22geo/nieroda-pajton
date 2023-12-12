def sort_select(elements):
    for i in range(len(elements)):
        min_value = i
        j=i+1
        while j < len(elements):
            if elements[j]<elements[min_value]:
                min_value = j
            j+=1
        
        elements[i] , elements[min_value] = elements[min_value], elements[i]
        i+=1
            
    return elements

elems = [5,2,3,1,4]
sorted_e = sort_select(elems)
print(str(sorted_e))