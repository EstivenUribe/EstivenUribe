<p align="right"><strong>English</strong> · <a href="./README.es.md" lang="es">Español</a></p>

# <img src="./assets/estiven-uribe.svg" width="39" height="39" alt=""> Rafael Estiven Uribe Álvarez

**Software developer · Backend and data integration**  
Medellín, Colombia

I’m a civil engineer completing a second degree in Informatics Engineering. I’ve connected billing software to Colombia’s tax authority and modeled university data. I’m looking for backend and data engineering roles in Colombia and on international teams.

## Featured projects

[RoadCare](#roadcare) · [Biblioteca Pro](#biblioteca-pro) · [Alerto](#alerto)

### RoadCare

**Road maintenance · Academic team project**  
Python · FastAPI · React · PostgreSQL

We built a web app that helps inspectors decide which road damage to address first. Its priority score accounts for severity, damage type and whether the site is in a critical zone. I worked on the repair workflow, from assigning a crew to having an inspector or administrator sign off on the completed work.

<img src="./assets/roadcare-priority.en.svg" width="430" alt="RoadCare example. A pothole with severity 3 out of 5 scores 9, medium priority, outside a critical zone and 13, high priority, inside one.">

[Source code][roadcare] · [Priority calculation][priority] · [User guide (Spanish)][road-guide]

### Biblioteca Pro

**End-to-end testing for a library catalog · Academic team project**  
Robot Framework · Selenium · Java · TestNG · Python

We automated browser tests for everyday library tasks, from finding a book by title or author to checking that canceling a deletion keeps it in the catalog. The suites read test cases from Excel. I improved the Windows launcher the team uses to run the tests and inspect screenshots.

[Source code and setup][qa] · [Catalog tests][catalog-tests] · [Windows launcher][qa-launcher]

### Alerto

**Civic alert API for Medellín · Academic team project**  
C# · ASP.NET Core · Entity Framework Core · PostgreSQL · Redis

The API records weather readings from Open-Meteo and can create a geolocated alert when rainfall risk is high. I added the Docker setup that runs the API, database and cache together. An integration test follows an alert from sign-in through creation and approval.

[Source code][alerto] · [OpenAPI specification][alerto-spec] · [Alert workflow test][alerto-test]

## Technical skills

<img src="./assets/icons/code.svg" width="18" height="18" alt=""> **Languages** · Python, JavaScript, C#, Java and SQL.

<img src="./assets/icons/layers.svg" width="18" height="18" alt=""> **Frameworks and libraries** · FastAPI and React for RoadCare, ASP.NET Core and Entity Framework Core for Alerto, and Spring Boot for electronic invoicing.

<img src="./assets/icons/database.svg" width="18" height="18" alt=""> **Databases and caching** · PostgreSQL for application records and Redis for cached API responses.

<img src="./assets/icons/terminal.svg" width="18" height="18" alt=""> **Development and testing** · Git, Docker Compose and OpenAPI, plus [end-to-end browser tests with Robot Framework and Selenium][qa].

<img src="./assets/icons/cloud.svg" width="18" height="18" alt=""> **Cloud, networking and security** · Supabase for university course scheduling, JWT for API access, and coursework in Linux and network security.

<img src="./assets/icons/network.svg" width="18" height="18" alt=""> **AI and machine learning** · In a deep learning course, my team used PyTorch and pix2pix to translate maps into satellite-style images. We compared the results when we changed the weight of the L1 loss.

## Experience and education

**Politécnico Colombiano Jaime Isaza Cadavid · Data analysis and architecture**  
I analyzed trends in academic records and prepared institutional reports. In my data architecture role, I modeled data from internal systems and external APIs and automated data validation and cleaning with Python and SQL.

**Eco-Tributario · Junior full-stack developer**  
I developed the local invoicing interface and used Spring Boot to connect the Saint business system to DIAN, Colombia’s tax authority, for electronic invoicing.

**Education** · Civil Engineering degree and final-semester Informatics Engineering studies at Politécnico Colombiano Jaime Isaza Cadavid. Admitted to the master’s program in Systems Engineering at Universidad Nacional de Colombia.

## Certifications & digital badges

| Badge | Credential and issuer |
| :--: | :-- |
| [<img src="./assets/badges/cisco-data-analytics.png" width="56" alt="Verify Data Analytics Essentials">][badge-data] | **[Data Analytics Essentials][badge-data]**<br>Cisco · Networking Academy |
| [<img src="./assets/badges/cisco-linux.png" width="56" alt="Verify Linux Essentials">][badge-linux] | **[Linux Essentials][badge-linux]**<br>Cisco · Networking Academy |
| [<img src="./assets/badges/cisco-ethical-hacker.png" width="56" alt="Verify Ethical Hacker">][badge-ethical] | **[Ethical Hacker][badge-ethical]**<br>Cisco · Networking Academy |
| [<img src="./assets/badges/certiport-generative-ai.png" width="56" alt="Verify Generative AI Foundations">][badge-genai] | **[Critical Career Skills - Generative AI Foundations][badge-genai]**<br>Certiport, a Pearson VUE business |
| [<img src="./assets/badges/coursera-watson.png" width="56" alt="Verify the Watson APIs badge">][badge-watson] | **[Creación de aplicaciones de IA con las API de Watson][badge-watson]**<br>Coursera (SENATEC program) |

## Contact

[LinkedIn][linkedin] · [estiven9512@gmail.com][email] · [Himalayas professional profile][himalayas]

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
