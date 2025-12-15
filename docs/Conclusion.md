### Reflexión personal: Medidas de seguridad en los lenguajes de programación

La frase de Bruce Schneier que aparece al principio de la unidad me parece super acertada: 
> El lenguaje que elijas para programar es como la cerradura de tu casa

De eso depende mucho la seguridad de lo que construyas. Después de leer el material de la Unidad 1 , me ha quedado claro que no todos los lenguajes tienen el mismo nivel de protección contra errores que luego pueden convertirse en vulnerabilidades.

Por ejemplo, los lenguajes de bajo nivel como C o el ensamblador dan mucho control, pero no te ayudan casi nada con la seguridad. Todo lo tienes que gestionar tú: la memoria, los punteros... Un despiste y tienes un problema, que puede ser una vulnerabilidad peligrosa.

En cambio, lenguajes de alto nivel como Python o Java te quitan mucho peso de encima. Eso evita un montón de errores clásicos. Java va más allá con su máquina virtual: verifica el bytecode, tiene sandbox, controla los accesos... Es más difícil que un programa Java tenga ciertos tipos de fallos de seguridad por diseño.

Luego están los lenguajes más modernos como Rust, que me parece impresionante. Lo que más llama la atención es que te obliga a manejar la memoria de forma segura desde el momento de compilar. Básicamente, elimina en tiempo de compilación errores que en C aparecerían en ejecución y podrían ser explotados. Go también ayuda bastante con su garbage collector y el detector de race conditions, aunque no llega al nivel de Rust.

Al final, creo que para proyectos donde la seguridad es crítica, merece la pena elegir lenguajes que incorporen protecciones de por si. No digo que abandonemos las de bajo nivel del todo, porque a veces hace falta para ciertas cosas de bajo nivel, pero siempre con mucho cuidado. Para la mayoría de aplicaciones nuevas, yo aplicaria Rust o Java o Go o python no tengo ni idea de como se usan pero son las mas seguras de usar (De python se algo  mas pero  tampoco gran cosa).

### Tabla comparativa de seguridad

| Lenguaje | Tipo/Nivel      | Medidas de seguridad principales                  | Vulnerabilidades comunes        | Recomendación           |
|----------|-----------------|---------------------------------------------------|----------------------------------------|------------------------------------------|
| C        | Compilado/Bajo  | Ninguna automática (gestión manual)               | Buffer overflow, use-after-free        | Solo para componentes críticos de bajo nivel con auditorías exhaustivas |
| Python   | Interpretado/Alto | Garbage collection, módulos seguros               | Inyecciones, errores runtime           | Excelente para scripting y prototipado seguro |
| Java     | Híbrido/Alto    | Verificación bytecode, sandbox JVM                | Deserialización insegura               | Ideal para aplicaciones enterprise      |
| Rust     | Compilado/Alto  | Ownership, borrow checker (memory safety)         | Muy pocas (seguro por diseño)          | Preferido para software crítico y seguro |
| Go       | Compilado/Alto  | Garbage collection, race detector                 | Errores de concurrencia menores        | Bueno para servicios y microservicios   |

