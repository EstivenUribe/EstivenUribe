<p align="right"><samp><a href="https://github.com/EstivenUribe" lang="en">English</a> · <strong>Español</strong></samp></p>

<h1><picture>
  <source media="(max-width: 680px) and (prefers-reduced-motion: no-preference)" srcset="./assets/identity/estiven-terminal-mobile-scan.svg">
  <source media="(max-width: 680px)" srcset="./assets/identity/estiven-terminal-mobile.svg">
  <source media="(prefers-reduced-motion: no-preference)" srcset="./assets/identity/estiven-terminal-scan.svg">
  <img src="./assets/identity/estiven-terminal.svg" width="100%" alt="Rafael Estiven Uribe Álvarez · Backend, APIs, SQL · Medellín, Colombia">
</picture></h1>

<p align="left">
  <a href="https://www.credly.com/badges/1fbcc50e-c05f-4293-bd6c-fbe96bf01fd8"><img src="./assets/badges/cisco-data-analytics.png" width="88" alt="Cisco Networking Academy · Data Analytics Essentials" title="Cisco Networking Academy · Data Analytics Essentials"></a>&nbsp;<a href="https://www.credly.com/badges/60cba0d4-ddd4-47a2-8194-0f593347344d"><img src="./assets/badges/cisco-linux.png" width="88" alt="Cisco Networking Academy · Linux Essentials" title="Cisco Networking Academy · Linux Essentials"></a>&nbsp;<a href="https://www.credly.com/badges/064f6c27-0a67-4558-b8df-3bf5637a909b"><img src="./assets/badges/cisco-ethical-hacker.png" width="88" alt="Cisco Networking Academy · Ethical Hacker" title="Cisco Networking Academy · Ethical Hacker"></a>
  <a href="https://www.credly.com/badges/a139445c-dfc9-406d-8b25-26b90a69bdf1"><img src="./assets/badges/certiport-generative-ai.png" width="88" alt="Certiport (Pearson VUE) · Critical Career Skills - Generative AI Foundations" title="Certiport (Pearson VUE) · Critical Career Skills - Generative AI Foundations"></a>&nbsp;<a href="https://www.credly.com/badges/9a5901c3-b913-41b9-ae86-4d5d372ff28b"><img src="./assets/badges/coursera-watson.png" width="88" alt="Coursera (SENATEC) · Creación de aplicaciones de IA con las API de Watson" title="Coursera (SENATEC) · Creación de aplicaciones de IA con las API de Watson"></a>
</p>

<details>
<summary><samp>Credenciales y emisores en Credly</samp></summary>

- **[Data Analytics Essentials][badge-data]** · Cisco Networking Academy
- **[Linux Essentials][badge-linux]** · Cisco Networking Academy
- **[Ethical Hacker][badge-ethical]** · Cisco Networking Academy
- **[Critical Career Skills - Generative AI Foundations][badge-genai]** · Certiport (Pearson VUE)
- **[Creación de aplicaciones de IA con las API de Watson][badge-watson]** · Coursera (SENATEC)

</details>

**Soy desarrollador de software y trabajo en sistemas backend e integración de datos.** Integré un sistema de facturación con la DIAN y automaticé la validación de registros universitarios con Python y SQL. Curso la Especialización en Inteligencia Artificial en la Universidad Nacional de Colombia.

## <samp>Proyectos destacados</samp>

[RoadCare](#roadcare) · [Biblioteca Pro](#biblioteca-pro) · [Alerto](#alerto)

### <samp>RoadCare</samp>

**¿Qué daño en la vía debería atender primero una cuadrilla?**<br><samp>Python · FastAPI · React · PostgreSQL</samp>

En la universidad desarrollamos una herramienta que prioriza los daños según su severidad, el tipo de daño y si la vía está en una zona crítica. [Trabajé en el flujo de reparación][road-work], desde la asignación de la cuadrilla hasta la aprobación del cierre por parte de un inspector o administrador.

<picture>
  <source media="(prefers-reduced-motion: no-preference)" srcset="./assets/roadcare-priority-motion.es.svg">
  <img src="./assets/roadcare-priority.es.svg" width="440" alt="El mismo bache, con severidad 3 de 5, obtiene 9 puntos fuera de una zona crítica (prioridad media) y 13 dentro de ella (prioridad alta).">
</picture>

[Repositorio][roadcare] · [Cálculo de prioridad][priority] · [Manual de usuario][road-guide]

### <samp>Biblioteca Pro</samp>

**¿El libro sigue en el catálogo si se cancela su eliminación?**<br><samp>Robot Framework · Selenium · Java · TestNG · Python</samp>

Es uno de los casos que automatizamos en el navegador, junto con las búsquedas por título y autor. Las pruebas toman sus datos de Excel. [Mejoré la interfaz de Windows][qa-work] que usa el equipo para ejecutarlas y revisar las capturas de pantalla.

[Repositorio e instalación][qa] · [Pruebas del catálogo][catalog-tests] · [Interfaz de Windows][qa-launcher]

### <samp>Alerto</samp>

**¿Cómo se convierte una lectura de lluvia en una alerta local?**<br><samp>C# · ASP.NET Core · Entity Framework Core · PostgreSQL · Redis</samp>

Nuestra API guarda lecturas de Open-Meteo y puede generar una alerta georreferenciada cuando hay riesgo alto por lluvias en Medellín. [Añadí la configuración de Docker][alert-work] para ejecutar juntos la API, la base de datos y la caché. Una prueba de integración recorre el inicio de sesión, la creación de la alerta y su aprobación.

[Repositorio][alerto] · [Especificación OpenAPI][alerto-spec] · [Prueba del flujo de alertas][alerto-test]

## <samp>IA aplicada</samp>

**¿Cómo se genera una vista aérea a partir de un mapa de calles?**<br><samp>PyTorch · pix2pix · U-Net</samp>

En un proyecto de clase, mi equipo hizo una prueba piloto con pix2pix usando pares de mapas y fotos aéreas. Cambiamos de 100 a 10 el peso del error píxel a píxel (L1) y comparamos ambos modelos con los mismos mapas. El esquema muestra cómo la U-Net conserva detalles de las calles al pasarlos del codificador al decodificador.

<picture>
  <source media="(prefers-reduced-motion: no-preference)" srcset="./assets/ai/pix2pix-motion.svg">
  <img src="./assets/ai/pix2pix.svg" width="468" alt="Esquema de pix2pix. Un mapa de calles entra en una U-Net. Las conexiones de salto llevan detalles al decodificador para generar una imagen de aspecto aéreo.">
</picture>

[Volver a ver la U-Net en movimiento][replay-pix2pix] · [Resultados del piloto (CSV)](./assets/ai/pix2pix-pilot.csv) · [Artículo original][pix2pix-paper]

## <samp>Competencias técnicas</samp>

<img src="./assets/icons/code.svg" width="18" height="18" alt=""> **Lenguajes** · Python, JavaScript, C#, Java y SQL.

<img src="./assets/icons/layers.svg" width="18" height="18" alt=""> **Frameworks** · FastAPI y React en RoadCare, ASP.NET Core y Entity Framework Core en Alerto, y Spring Boot en facturación electrónica.

<img src="./assets/icons/database.svg" width="18" height="18" alt=""> **Bases de datos y caché** · PostgreSQL para los registros de las aplicaciones y Redis para almacenar respuestas de la API en caché.

<img src="./assets/icons/terminal.svg" width="18" height="18" alt=""> **Desarrollo y pruebas** · Git, Docker Compose, OpenAPI y [pruebas de extremo a extremo con Robot Framework y Selenium][qa].

<img src="./assets/icons/cloud.svg" width="18" height="18" alt=""> **Nube, redes y seguridad** · Supabase para la programación de cursos universitarios, JWT para el acceso a la API y formación en Linux y seguridad de redes.

<img src="./assets/icons/network.svg" width="18" height="18" alt=""> **Aprendizaje automático** · PyTorch para transformar imágenes y TensorFlow/Keras para pronosticar secuencias.

## <samp>Experiencia y formación</samp>

**Eco-Tributario · Desarrollador full stack junior**<br>Desarrollé la interfaz local de facturación e integré el sistema administrativo Saint con la DIAN mediante Spring Boot para la facturación electrónica.

**Politécnico Colombiano Jaime Isaza Cadavid · Análisis y arquitectura de datos**<br>Analicé tendencias en registros académicos y preparé informes institucionales. Como arquitecto de datos, modelé información de sistemas internos y API externas y automaticé la validación y limpieza de datos con Python y SQL.

**Universidad Nacional de Colombia · Especialización en Inteligencia Artificial (en curso)**<br>En un ejercicio de aprendizaje profundo usé una LSTM para pronosticar una onda seno. Cada predicción volvía a entrar al modelo para calcular la siguiente. En los primeros 40 pasos, la raíz del error cuadrático medio fue **0,0206 con diez muestras previas** y **1,0835 con una sola**. Una misma altura puede corresponder a un tramo ascendente o descendente de la onda.

<picture>
  <source media="(prefers-reduced-motion: no-preference)" srcset="./assets/ai/lstm-window-motion.svg">
  <img src="./assets/ai/lstm-window.svg" width="468" alt="Una ventana móvil resalta diez muestras consecutivas de la onda seno original que recibe la LSTM.">
</picture>

[Volver a ver la ventana en movimiento][replay-lstm] · [Resultados del ejercicio (CSV)](./assets/ai/lstm-window-results.csv)

**Ingeniería Informática** · Curso el último semestre en el Politécnico Colombiano Jaime Isaza Cadavid. También soy ingeniero civil.

## <samp>Contacto</samp>

Busco oportunidades en desarrollo backend e ingeniería de datos en Colombia y en equipos internacionales.

[LinkedIn][linkedin] · [estiven9512@gmail.com][email] · [Perfil profesional en Himalayas][himalayas]

<sub>La portada muestra el relieve de Medellín y sus alrededores. Datos de elevación de <a href="https://topotools.cr.usgs.gov/gmted_viewer/viewer.htm">USGS y NGA, GMTED2010</a>.</sub>

[roadcare]: https://github.com/EstivenUribe/RoadCare
[priority]: https://github.com/EstivenUribe/RoadCare/blob/main/backend/app/services/ai_priority.py
[road-guide]: https://github.com/EstivenUribe/RoadCare/blob/main/docs/manual_usuario.md
[catalog-tests]: https://github.com/EstivenUribe/test-roboframework/blob/main/robot/tests/02_catalogo.robot
[qa-launcher]: https://github.com/EstivenUribe/test-roboframework/blob/main/gui/launcher.py
[alerto]: https://github.com/EstivenUribe/Alerto
[alerto-spec]: https://github.com/EstivenUribe/Alerto/blob/main/alerto-openapi.yaml
[alerto-test]: https://github.com/EstivenUribe/Alerto/blob/main/tests/Alerto.IntegrationTests/AlertWorkflowTests.cs
[qa]: https://github.com/EstivenUribe/test-roboframework
[badge-data]: https://www.credly.com/badges/1fbcc50e-c05f-4293-bd6c-fbe96bf01fd8
[badge-linux]: https://www.credly.com/badges/60cba0d4-ddd4-47a2-8194-0f593347344d
[badge-ethical]: https://www.credly.com/badges/064f6c27-0a67-4558-b8df-3bf5637a909b
[badge-genai]: https://www.credly.com/badges/a139445c-dfc9-406d-8b25-26b90a69bdf1
[badge-watson]: https://www.credly.com/badges/9a5901c3-b913-41b9-ae86-4d5d372ff28b
[linkedin]: https://www.linkedin.com/in/rafaeluribealvarez/
[email]: mailto:estiven9512@gmail.com
[himalayas]: https://himalayas.app/@estivenuribealvarez
[road-work]: https://github.com/EstivenUribe/RoadCare/commit/7ddc2b8587e85e0f08a93039824f2dafd2d2b54f
[qa-work]: https://github.com/EstivenUribe/test-roboframework/commit/d967f6b1bd2eb03b1dae9db2554b4a3377ca8cd8
[alert-work]: https://github.com/EstivenUribe/Alerto/commit/384a84ac7c516d1fe3af4979eadafd0aad14305f
[pix2pix-paper]: https://phillipi.github.io/pix2pix/
[replay-pix2pix]: https://raw.githubusercontent.com/EstivenUribe/EstivenUribe/main/assets/ai/pix2pix-motion.svg
[replay-lstm]: https://raw.githubusercontent.com/EstivenUribe/EstivenUribe/main/assets/ai/lstm-window-motion.svg
