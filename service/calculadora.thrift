namespace php calculadora

exception OperacionIvalida {
    1: string mensaje
}

service calculadora{

    double division(1: i32 dividendo, 2: i32 divisor) throws (1: OperacionIvalida operacionInvalida),

    i32 suma(1: i32 numero1, 2: i32 numero2) throws (1: OperacionIvalida operacionInvalida),

    i32 multiplicacion(1: i32 numero1, 2: i32 numero2) throws (1: OperacionIvalida operacionInvalida),

    i32 resta(1: i32 minuendo, 2: i32 sustraendo) throws (1: OperacionIvalida operacionInvalida)
}