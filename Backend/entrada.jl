function factorial(num::Int64)::Int64
    if num == 1
        return 1;
    else
        return factorial(num - 1)*num;
    end;
end;

println(factorial(5));
