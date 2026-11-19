# Phoenix — resume and job search

**Status:** Active — started 2026-11-14
**Goal:** Build a strong resume for Leroy and apply to roles. Each target job gets its own file in `phoenix/`, and the resume is tailored per role.

## Target jobs

| Job | Company | Location | Apply by | Status | File |
| --- | --- | --- | --- | --- | --- |
| Manager, Site Reliability Engineering (JREQ205128) | Thomson Reuters | Hybrid, Eagan, MN | 2026-12-04 | Not applied | [phoenix/thomson-reuters-sre-manager.md](phoenix/thomson-reuters-sre-manager.md) |

## Files

- [phoenix/career-notes.md](phoenix/career-notes.md) — full structured career notes (source material).
- [phoenix/resume-master.md](phoenix/resume-master.md) — editable resume source. [phoenix/resume-master.html](phoenix/resume-master.html) is the print copy, rebuilt from the Markdown when it changes. **Renders to one page** (checked 2026-11-14).

- [phoenix/TR Resume.md](<phoenix/TR Resume.md>) — two-page resume tailored to the Thomson Reuters SRE Manager posting (2026-11-14). [phoenix/TR Resume.html](<phoenix/TR Resume.html>) is its print copy. The master resume files are unchanged and still lack the LinkedIn URL.
- LinkedIn: https://www.linkedin.com/in/leroy-dehnke-b0759467/
- **Leroy asked that career-notes.md not be edited further** (2026-11-14).

## Corrections from Leroy, 2026-11-14 (applied to both resumes and the cover letter)

- **No SLAs, anywhere.** He never worked on a team with a customer SLA. Internally there were SLIs and SLOs only. The word "SLA" must not appear on any resume or letter. (`career-notes.md` still says "SLAs and SLIs" in one line, but he asked that it not be edited.)
- **Incident Manager:** he has acted as Incident Manager at both Vanco and Finalsite.
- **PagerDuty:** the migration did include escalation policies and stakeholder communications.
- **Terraform, Bicep, ARM:** never hands-on (corrected 2026-11-15). He led the teams that set them up. The resumes and letter say he led those teams, and the skills lines say "team-led infrastructure as code." He **is** hands-on with Azure DevOps.
- **Postmortems:** he ran them.
- **24x7 on-call:** he was on 24x7 on-call for some of his time at Vanco.
- **PCI platform:** Azure only.
- **AI rollout timing (2026-11-15):** GitHub Copilot and Claude Code were introduced to the teams during the Sr Manager/Director period, not the manager years. (`career-notes.md` still implies Copilot came with the analytics system. It was left unedited at his request.) The analytics system itself was built in the manager years.
- **TR resume trims (2026-11-15):** Education is the Brown AAS line only (no U of M, no A+), the Skills section was removed, and Monday.com is deliberately left off.
- **Education:** CompTIA A+ Certified Professional is now on both resumes, with no date. The 4.0 GPA stays notes-only.
- **LinkedIn link:** added to the master resume too.

Still unconfirmed: **corrective action planning** as part of the postmortem process (the TR resume lists it).

## Ground rules (from Leroy)

- **LinkedIn dates and titles are authoritative.** The one exception is Finalsite, which isn't on LinkedIn yet: keep the name and the 2026-07-16 start date.
- One page. No college graduation year. Anything before 2010 stays vague and brief.
- 2015–2018 as Software Developer was individual contributor work with no direct reports. Management resumed in 2018.
- Managing people: 2008–2014 and 2018–present, about 14 years in total. This corrects my earlier "about 18 years".

## Resolved

- Director start date is Nov 2025 (LinkedIn), not 2026-03-18 as in the work wiki (separate repo).
- Title is "Sr Enterprise Data Team Manager," and the Software Developer start is 2015-01.
- "KLM" is **KQL** (Kusto Query Language), used by Azure Application Insights.
- The work wiki's `people/leroy-dehnke.md` still has the old dates and titles. That is work-wiki content (separate repo), so it was not touched. Align it there if wanted.

## Answered 2026-11-14

- **Contact:** phone 612-385-3405, email leroydehnke@gmail.com. Show "Rosemount, MN" only, no full address.
- **Overlap:** Sr Manager and Director on one line is fine.
- **ACST acquisition:** happened during the Sr Manager/Director period, probably fall 2025. No exact date on the resume; it sits in that section.
- **Re-org (one team to three):** during the manager period. No date.
- **Tempo:** Jira time-tracking add-on.
- **No metrics.** Leroy has no numbers to offer and doesn't want one or two stray figures. The resume only uses sizes and counts he gave.
- **VancoPay:** did not launch. It was cancelled by C-level management, not the team's fault. Left off the "launched" story; the resume only says he built it.
- **Infrastructure as code:** Bicep and ARM in the manager period (with SREs on the team). Terraform in the last phase at Finalsite.
- **Languages:** Python added to the Software Developer era. Java left off.
- **Current SRE scope:** six products. Four all Azure, one all AWS, one half Azure and half AWS.
- **Not experienced with:** GCP, Datadog, New Relic. Don't claim them.
- **Added to Manager and Sr Manager sections:** hiring, performance reviews, coaching and career development, promotions, and presenting architecture plans and project updates to executives.
- **Added to Sr Manager:** selecting and managing contractors (project-based and staff augmentation), including one firm for the Salesforce cleanup, and coordinating projects with teams in South America, Central America, Europe, Asia, and Australia.
- **Cover letter:** wanted. Draft in [phoenix/cover-letter-thomson-reuters.md](phoenix/cover-letter-thomson-reuters.md).

## Open items

- **LinkedIn URL** for the contact line. Not on the resume until provided.
- **Cover letter facts:** it mentions that you live close to Eagan. Remove if you'd rather not.
- **Optional examples** (no numbers needed): a major incident you led, how you present to executives, and someone you coached into a promotion.

## Next steps

- [x] Capture career history and brain dump
- [x] Draft the master one-page resume (renders to one page, 2026-11-14)
- [x] Draft the cover letter
- [ ] Leroy reviews the resume and cover letter
- [ ] Tailor the resume to the Thomson Reuters posting
- [ ] Apply by 2026-12-04
