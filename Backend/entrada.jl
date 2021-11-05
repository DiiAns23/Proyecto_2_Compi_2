mutable struct Hijo
    nombre::String;
    apellido::String;
    edad::Int64;
end;

mutable struct Padre
    nombre::String;
    apellido::String;
    hijos::Vector{Hijo};
end;

diego = Hijo("Diego","Obin",20);
jose = Hijo("Jose","Obin",17);

hijos = [diego, jose]::Vector{Hijo};

padre = Padre("Juan","Obin",hijos);

print(padre.hijos[1].nombre);

