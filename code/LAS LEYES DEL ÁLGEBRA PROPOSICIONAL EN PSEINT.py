Algoritmo TablaDeVerdad
    // Definir variables
    Dimension combinaciones(8, 3)
    Dimension resultados(8, 6)
	
    // Asignar combinaciones de valores de verdad
    combinaciones[1,1] <- Verdadero; combinaciones[1,2] <- Verdadero; combinaciones[1,3] <- Verdadero
    combinaciones[2,1] <- Verdadero; combinaciones[2,2] <- Verdadero; combinaciones[2,3] <- Falso
    combinaciones[3,1] <- Verdadero; combinaciones[3,2] <- Falso; combinaciones[3,3] <- Verdadero
    combinaciones[4,1] <- Verdadero; combinaciones[4,2] <- Falso; combinaciones[4,3] <- Falso
    combinaciones[5,1] <- Falso; combinaciones[5,2] <- Verdadero; combinaciones[5,3] <- Verdadero
    combinaciones[6,1] <- Falso; combinaciones[6,2] <- Verdadero; combinaciones[6,3] <- Falso
    combinaciones[7,1] <- Falso; combinaciones[7,2] <- Falso; combinaciones[7,3] <- Verdadero
    combinaciones[8,1] <- Falso; combinaciones[8,2] <- Falso; combinaciones[8,3] <- Falso
	
    // Encabezados de la tabla
    Escribir "A", "B", "C", "~C", "B | ~C", "A & (B | ~C)"
    Escribir "----------------------------------------"
	
    // Calcular y mostrar la tabla de verdad
    Para i <- 1 Hasta 8 Con Paso 1 Hacer
        A <- combinaciones[i, 1]
        B <- combinaciones[i, 2]
        C <- combinaciones[i, 3]
        not_C <- No C
        B_or_not_C <- B O not_C
        resultado <- A Y B_or_not_C
        
        // Almacenar resultados
        resultados[i,1] <- A
        resultados[i,2] <- B
        resultados[i,3] <- C
        resultados[i,4] <- not_C
        resultados[i,5] <- B_or_not_C
        resultados[i,6] <- resultado
		
        // Mostrar resultados de la fila actual
        Escribir A, "  ", B, "  ", C, "  ", not_C, "  ", B_or_not_C, "  ", resultado
    FinPara
FinAlgoritmo