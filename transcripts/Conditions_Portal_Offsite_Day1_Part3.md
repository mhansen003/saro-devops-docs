# Conditions Portal Offsite - Day 1 Meeting Minutes

**Date:** January 13, 2026  
**Location:** CMG Financial Office (with remote participants)  
**Duration:** ~5 hours (Part 1: 2h 37m, Part 2: 2h 35m)  
**Facilitator:** Mark (Product Leadership)  
**Recorder:** Leslie Chang

---

## Attendees

### In-Person
- Mark (Product Leadership)
- Leslie Chang (AI Program Manager, POC Lead)
- Tim Borquez (Design)
- Josephine Yen (Product/Data Model)
- Toni (Mortgage SME)
- Jina Choi (Candor Integration Lead)
- Kitt Holland (Engineering)
- Rusty (Engineering Lead)
- Annie (Product)

### Remote
- Carlos Sanchez (Engineering)
- Shailendra Sharma (Engineering/Product)
- Kelly Mattox (Byte Platform Owner) - joined afternoon session

---

## Meeting Objective

Align product and engineering teams on Conditions Portal requirements, demonstrate the working prototype, establish phase 1 scope, and develop implementation strategy for one of CMG's top three initiatives for 2026.

---

## High-Level Summary

The Conditions Portal is a modernization initiative to replace the outdated Byte conditions interface with a unified, user-friendly portal for all loan condition management. The project aims to streamline workflows for loan officers, processors, underwriters, funders, and post-closing teams. Day 1 focused on prototype demonstration, feature review, data model discussion, and addressing integration challenges with the existing Byte system.

Key themes emerged around:
1. Using Claude/AI tools to accelerate development
2. Managing the complexity of role-based permissions
3. Ensuring backward compatibility with Byte while adding new functionality
4. Planning a phased rollout strategy to minimize disruption

---

## Key Features Reviewed

### Core Functionality
- **Unified Conditions Dashboard** - Single portal for viewing/managing all loan conditions with role-based filtering (Active, Cleared, Ready for Underwriting)
- **Condition Management** - Create, edit, link documents, change status, add notes, set flags
- **Document Workflow** - Upload, split, merge, rotate documents; associate documents to multiple conditions (many-to-many relationship - deviation from Byte)
- **Notes System** - Three levels: loan notes, condition notes, and document notes with read/unread indicators per user
- **Automated Conditions Engine** - Rules-based condition generation that can run on-demand to add/remove conditions based on loan criteria

### Borrower Communication
- **AI-Generated Email Requests** - Draft borrower document request emails with AI-assisted tone selection (formal, casual, friendly)
- **Email Templates** - Save and manage custom email templates
- **Auto-Reminders** - Configurable follow-up reminders for outstanding document requests

### User Experience
- **Wizard Mode** - Step-through workflow for reviewing documents and clearing conditions
- **Custom Condition Lists** - Users can save frequently-used condition sets (e.g., "Miami Condos," "FHA Loans")
- **Personal Flags** - User-specific color flags for self-organization (not visible to others)
- **Search and Filter** - Search by condition ID, keywords; filter by category, status, stage, flags

### Integration Points
- **Byte LOS Integration** - Opens within Byte via web control, passes loan context
- **Clear Docs Integration** - Shared document repository and management
- **Candor Integration** - Automated condition creation and clearance via OCR/AI
- **Borrower Needs List** - Existing tool to be wired into Conditions Portal

---

## Decisions Made

| # | Decision | Owner | Notes |
|---|----------|-------|-------|
| 1 | **Documents can link to multiple conditions** | Engineering | Deviation from Byte's 1:1 model; will require reconciliation logic |
| 2 | **Flags are user-specific, not global** | Product/Design | Personal organization tool, not communication mechanism |
| 3 | **Remove "Responsibility" field** | Kelly Mattox | Per Byte team direction; Candor will use "Transaction" field instead |
| 4 | **Notes system will be enhanced** | Engineering | Moving from single text blob to structured notes with timestamps and user attribution |
| 5 | **No save button - auto-save on action** | Product/Engineering | Terminal actions (accept, clear, reject) trigger saves |
| 6 | **Kill email tabs feature** | Product | Simplify UI; remove multiple AI-generated version tabs |
| 7 | **Product requirements due end of January** | Product Team | Using Sato's tool to create tickets in GitHub |
| 8 | **Build in Clear, accessible from Byte** | Engineering | Follow existing pattern (like Clear Docs, Pipeline) |
| 9 | **Support downstream roles (funders, closers, post-closing)** | Product | Minimize to ~7 base roles that map from 400+ Byte roles |

---

## Open Items / Action Items

| # | Item | Owner | Due Date | Priority |
|---|------|-------|----------|----------|
| 1 | Create role/permissions matrix (7-8 roles with actions allowed) | Josephine/Lauren | TBD | High |
| 2 | Map Byte roles to Conditions Portal base roles | Andrew (new employee) | TBD | High |
| 3 | Clarify "Responsibility" field removal impact on Candor | Jina Choi/Kelly | ASAP | High |
| 4 | Document Kelly's "Cardinal Rules" and constraints | Leslie/Tim | TBD | Medium |
| 5 | Investigate loan-level flag for beta rollout (conditions portal vs legacy) | Rusty/Engineering | TBD | Medium |
| 6 | Deep dive on Exception Requests functionality | Product/Kelly | TBD | Medium |
| 7 | Determine auto-run conditions engine trigger (on loan open vs button) | Product/Kelly | TBD | Medium |
| 8 | Add AI document auto-indexing (Sato's tool) to requirements | Leslie | End of Jan | Medium |
| 9 | Expedite Claude Code access for Josephine, Tim | Mark | This week | Low |
| 10 | Review document description field availability in split/merge | Tim/Engineering | TBD | Low |
| 11 | Confirm closer vs funder role distinction (wet state vs dry state) | Kelly/Lauren | TBD | Medium |
| 12 | Schedule Sato demo for Day 2 (SDLC tool) | Mark | Jan 14 | Done |

---

## Risks and Concerns

### High Priority

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Byte auto-save conflicts** | Users editing conditions in Byte could overwrite Conditions Portal data | Implement rollback/recovery mechanism; Conditions Portal is source of truth for its data |
| **Role/permission complexity** | 400+ Byte roles could create implementation nightmare | Consolidate to 5-7 base roles; map Byte roles at login |
| **Downstream department disruption** | Post-closing, QC, funders support all channels - can't isolate them to beta | Use loan-level flag to determine which UI opens; users may see both systems based on loan |
| **Data sync between Byte and Clear** | Hybrid data model (some data in Byte, some in Clear) adds complexity | API handles sync; audit logging for all changes; Domo reporting joins both sources |

### Medium Priority

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Candor dependency on "Responsibility" field** | Candor pilot may break if field is removed | Coordinate with Byte team; potentially use "Transaction" field instead |
| **Scope creep** | Project stalled before due to size | Mark's directive: everything in unless compelling reason to exclude |
| **AI token costs for email generation** | Potential runaway costs | Cost is negligible (fractions of a cent); remove generation limits |
| **Custom conditions bypass governance** | Users creating ad hoc conditions undermines standardization | Allow but monitor; mine custom conditions for patterns to standardize |

### Technical Concerns (Kelly Mattox)

1. **API user attribution** - Byte API shows system account, not individual user who made change
2. **Bidirectional sync timing** - ~30 second delay acceptable for updates between systems
3. **Existing pipeline compatibility** - Need to support both old and new systems during transition

---

## Rollout Strategy Discussion

The team discussed a **phased beta approach**:

1. **Create loan-level flag** in Byte to identify "Conditions Portal loans"
2. **Select pilot group** - Full value chain (LOs, processors, underwriters, closers, funders, post-closing) to avoid mid-loan handoff issues
3. **Modify Byte conditions button** - Check loan flag, open legacy or new portal accordingly
4. **Parallel operation** - Users may work both systems depending on which loans they're assigned
5. **Monitor and fix** - Run pilot for ~1 month before company-wide rollout

This follows precedent set by GFE/Loan Estimate toggle in Byte.

---

## Day 2 Agenda Preview

- Sato demo of SDLC tool (1:00 - 3:00 PM)
- Implementation strategy deep dive
- Engineering requirements discussion
- GitHub repo setup for Conditions Portal
- Create initial tickets using Sato's tool

---

## Attachments/References

- Bolt prototype (demonstrated by Leslie)
- Figma designs (Tim Borquez)
- Data model spreadsheet (Josephine Yen)
- Kelly Mattox's Cardinal Rules (to be documented)

---

*Minutes prepared by: Claude AI (from meeting transcripts)*  
*Distribution: All attendees, Lauren (Operations), Susan Walker (CPO)*
