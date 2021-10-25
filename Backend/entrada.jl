function swap(i::Int64, j::Int64, arr::List) 
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
end;

function bubbleSort(arr::List)
    for i in 0:(length(arr) - 1)
        for j in 1:(length(arr) - 1)
            if(arr[j] > arr[j + 1])
                swap(j, j+1, arr);
            end;
        end;
    end;
end;

arreglo = [32,7*3,7,89,56,909,109,2,9,9874^0,44,3,820*10,11,8*0+8,10];
bubbleSort(arreglo);

for i in 1:length(arreglo)
    println(arreglo[i]);
end;