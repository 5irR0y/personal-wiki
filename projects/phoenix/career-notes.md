# Phoenix — career notes (source material for the resume)

Source: Leroy's LinkedIn (pasted 2026-11-14) and his brain dump of the same day. **LinkedIn dates and titles are authoritative** (Leroy, 2026-11-14). The one exception: Finalsite isn't on LinkedIn yet, so the Finalsite name and the **2026-07-16** start date are kept.

## Timeline

One continuous employer since 2004-02-20. The name changed over time: RevTrak, then Connexeo (2018-06), then Vanco (2018-09 merger), then Finalsite (education business acquired 2026-07-16).

| Dates | Title | Managing people? |
| --- | --- | --- |
| 2004-02 to 2007-12 | Client Services and Network Support | No |
| 2008-01 to 2014-12 | Operations Manager | **Yes**, up to 10 (client support, merchant onboarding, merchant funding, fee invoicing) |
| 2015-01 to 2018-09 | Software Developer | **No.** He stepped from management back to individual contributor |
| 2018-10 to 2019-12 | Software Development Team Lead (Payments) | Yes, developers and SDETs |
| 2020-01 to 2024-12 | Software Development Manager (Payments) | Yes, up to 8 on one team, later up to 20 across 3 teams |
| 2025-01 to 2025-12 | Sr Enterprise Data Team Manager | Yes |
| 2025-11 to present | Director of Enterprise Data Team | Yes |
| 2026-07-16 to present | Finalsite employee (same Director role) | Yes |

Managing people: 2008–2014 and 2018–present, about 14 years in total. The earlier "about 18 years" figure was wrong because it ignored the developer years.

## Software Developer, 2015–2018 (individual contributor)

- On the team that designed and built a **PCI-compliant payments platform** (ConnexPoint, CXP). First live transaction 2017-05-19.
- Used internally, first at RevTrak and still by every company since, including Finalsite. Also offered as an **API** that outside companies use to process their payments.
- Written in **.NET / C#** and hosted in **Azure**.
- Became very proficient in **PowerShell** and **SQL**.

## Team Lead and Software Development Manager, 2018–2024

**Same CXP team, up to 8 people.** SREs and DBAs were embedded on the team and reported to him.
- Hired and promoted several people into SRE roles.
- Oversaw the **PCI audit**, with help from the compliance team.
- Built the **CI/CD pipeline** and the dev, QA, and stage environments, plus a **partner integration testing environment**. Reached about **one deployment per day**, because the platform is microservices and parts deploy independently.
- Set up **SLAs and SLIs from scratch**. Components had different uptime requirements, and the SREs reported to him.
- Brought in **OpsGenie** for alerting. He took equal turns on call with his SREs.
- **Observability:** Azure Application Insights, and he became proficient in its query language. The language is **KQL (Kusto Query Language)**. Leroy wrote "KLM"; I confirmed it's KQL.
- Data stores: Azure SQL, Redis, Azure Blob Storage, Azure Storage Tables.
- Acted as scrum master for the team.

**After a re-org and expansion (after 2020, when work went remote): 3 teams, up to 20 developers and QA.**
- Mostly local in MN, but **two of the three teams were in Mexico**.
- One team kept running CXP. The other two built a new payments platform, **VancoPay**: one on front end and mobile, one on the back end. The back end used **Cosmos DB** and **Service Bus** for an event-driven architecture.
- SREs and DBAs no longer reported to him at this point.
- Each team had its own scrum master. Leroy set up **cross-team deployment testing**, between his teams and with the other Vanco teams that used the payment platforms.
- Heavily involved in **product ownership, product management, and project management**.
- **Jira** for work and team metrics, **Monday.com** for leadership status reporting, **Confluence** as the source of truth.
- Wrote the team's **incident response plans and postmortems**.

**AI work:** Started using AI here. With **Copilot and Cursor** he built his own system that pulls data from **Jira, App Insights, Tempo, and Azure DevOps**, and stores metrics in a **SQL database** he built: uptime, deployment cadence, and team velocity. He also helped build out Azure DevOps for deployments. **GitHub Copilot** was introduced to the teams around the same time.

## Data team, 2025–present (Sr Manager, then Director)

- Stepped away from the development teams to lead the **DBAs and data engineers** who run **Snowflake** and all **SQL Server and MySQL** instances across the company.
- Up to **4 DBAs and 4 data engineers** at first. After Vanco acquired **ACST**, the Data Team reached **18 people**. Helped integrate the acquired company: consolidated tools and technologies where appropriate and streamlined processes.
- Introduced the **Data Team Review**: his team reviews every data change from any team before it goes to production.
- Helped develop and roll out the **Release Management Meeting (RMM)**, which all software teams go through as part of deployment. He is one of the **approvers on all deployments**.
- The **Salesforce** product and team moved into his department. He applied data management best practices and cleaned up Salesforce data that came from multiple product lines and acquisitions.

## Most recent: SREs and TechOps

Now supervises **all SREs and TechOps**. Consolidated SREs who used to work on individual products into **one team**: regular huddles, a **centralized Jira board**, moved alerting from **OpsGenie to PagerDuty**, and set up an **on-call rotation**.

## Education

- **University of Minnesota:** 3 years.
- **Brown College:** Associate of Applied Science in Information & Networking Technology. Degree awarded **2003-12-19**, GPA **4.0**.
- **Certification:** CompTIA A+ Certified Professional, earned **2003-11-12** while at Brown College.
- **Resume rules:** no graduation year. The GPA and the A+ certification are for these notes only, not the resume (Leroy, 2026-11-14).

## Resume rules from Leroy

- One page.
- No college graduation year.
- Anything before 2010 stays vague and brief.

## Open questions

See [../phoenix.md](../phoenix.md).
