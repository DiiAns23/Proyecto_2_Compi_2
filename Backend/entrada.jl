function factorial(num::Int64)
    if num ==1
        return 1;
    end;
    return num * factorial(num-1);
end;

print(factorial(5));
