Algoritmo G6_Ecuacion_Cuadrática 
	Definir a,b,c,base,x1,x2,r,i Como Real;
	Escribir "Bienvenido a la ecuación cuadrática";
	Escribir "Ingrese el valor de a";
	Leer a;
	Escribir "Ingrese el valor de b";
	Leer b;
	Escribir "Ingrese el valor de c";
	Leer c;
	base= ((b*b)-(4*a*c));
    Escribir "Base", base;
    Si (a = 0) Entonces
		Escribir "Error,no puedes dividir entre 0";
	SiNo
		Si (base >= 0) Entonces
		    x1 = (-b+raiz(base))/(2*a);
		    x2 = (-b-raiz(base))/(2*a);
		    Escribir "x1=", x1, "x2=", x2;
	    SiNo
		    Escribir "El resultado es imaginario";
		    r = (-b/(2*a));
		    i = raiz(-base)/(2*a);
			Escribir "x1=", r "+",i,"i";
	        Escribir "x2=", r "-",i,"i";
	    Fin Si
	Fin Si
FinAlgoritmo
