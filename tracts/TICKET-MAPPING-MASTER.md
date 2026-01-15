# CONDITIONS PORTAL - MASTER TICKET MAPPING
## Complete Ticket Structure with Dependencies

**Last Updated:** January 2026
**POC Source:** https://conditions-portal-pr-ahby.bolt.host/

---

## TIER 1: PLATFORM FOUNDATION (CP-001 to CP-099)

### #CP-001 - Conditions Grid Platform (Read-Only)
- **Type:** Platform
- **Size:** Large (8+ hours)
- **Depends On:** None
- **Blocks:** CP-100, CP-200, CP-300, CP-400
- **Components:**
  - Grid component with virtual scrolling
  - Stage grouping (SUSP, PTD, PTF, PTP, POST, TRAIL)
  - Column headers (Category, Description, Status, Notes, Doc Requests, Docs)
  - Bulk selection checkboxes
  - API: GET /api/loans/{loanId}/conditions
  - Data models: Condition, StatusHistory, DocumentRequest
- **Acceptance Criteria:**
  - Grid displays all conditions grouped by stage
  - Read-only view (no mutations)
  - API integration complete
  - Responsive layout works on desktop
  - Loads within 2 seconds for 100+ conditions

---

## TIER 2: ROLE SCAFFOLDING (CP-100, CP-200, CP-300)

### #CP-100 - Processor Role Shell
- **Type:** Role
- **Size:** Medium (4-6 hours)
- **Depends On:** CP-001
- **Blocks:** CP-101 through CP-118
- **Components:**
  - Processor-specific filter pills container
  - Action buttons panel (placeholder)
  - Role-based permission checks
  - Route: /processor/conditions
- **Acceptance Criteria:**
  - Processor view shows correct filtered conditions (Class: "Processor III")
  - 5 filter pills visible: Active, Need to Request, Requested, Send Brw Requests, Review Docs
  - Action panel renders but buttons are placeholders
  - Permission check prevents underwriter-only actions

### #CP-200 - Underwriter Role Shell
- **Type:** Role
- **Size:** Medium (4-6 hours)
- **Depends On:** CP-001
- **Blocks:** CP-201 through CP-204
- **Components:**
  - Underwriter-specific filter pills container (simplified)
  - Decision action panel (placeholder)
  - Route: /underwriter/conditions
- **Acceptance Criteria:**
  - Underwriter view shows correct filtered conditions (Class: "UW")
  - 2 filter pills visible: Active, Review Docs
  - Simplified UI focused on approval/rejection decisions
  - Permission check prevents processor-only actions

### #CP-300 - Borrower Role Shell
- **Type:** Role
- **Size:** Medium (4-6 hours)
- **Depends On:** CP-001
- **Blocks:** CP-301 through CP-304
- **Components:**
  - Borrower-facing portal view
  - Document upload area (placeholder)
  - Status timeline view
  - Route: /borrower/conditions
- **Acceptance Criteria:**
  - Borrower sees only conditions marked Type: "BRW"
  - Simplified language (no internal jargon)
  - Upload placeholder visible
  - Mobile-responsive

---

## TIER 3: PROCESSOR FEATURES (CP-101 to CP-118)

### #CP-101 - Add Document Request with Rich Text
- **Type:** Feature
- **Size:** Small (2-3 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - "Add request" button on each condition row
  - Modal: Add Document Request
  - Document Type dropdown (16 predefined types)
  - Request For selector (borrower names)
  - Rich text editor (Bold, Italic, Underline, Link) with character count (0/1000)
  - API: POST /api/conditions/{conditionId}/document-requests
- **Acceptance Criteria:**
  - Modal opens when "Add request" clicked
  - Dropdown shows 16 document types (Appraisal, Asset Statements, Bank Statements, etc.)
  - Rich text editor supports formatting
  - Character limit enforced at 1000
  - Request created and appears in Outstanding Document Requests section

### #CP-102 - Edit Condition - Full CRUD
- **Type:** Feature
- **Size:** Medium (4-5 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - Click condition ID to open Edit Condition modal
  - Form fields: Name, Description, Category (disabled), Number (disabled), Status, Stage, Class, Type (INT/BRW)
  - Accordion sections: Set Flag, Outstanding Document Requests, Exception Request, Dates, Status History, Condition Notes
  - Save/Cancel buttons
  - API: PUT /api/conditions/{conditionId}
- **Acceptance Criteria:**
  - All fields pre-populated from current condition data
  - Status change records timestamp in status history
  - Stage change moves condition to new stage group
  - All accordion sections functional
  - Validation prevents empty required fields

### #CP-103 - Add Conditions from Template Library
- **Type:** Feature
- **Size:** Medium (5-6 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - "Add Conditions" button in header
  - 3-panel modal: My Lists & Categories (left), Available Conditions (middle), Current Conditions (right)
  - 20+ category buttons (APP, DISC, CRED, INC, ASSET, PROP, MISC, CLSNG, TITLE, GOV, BOND, SP, CONDO, etc.)
  - Search box with real-time filtering
  - "Custom" button to create new template
  - "Add" and "Remove" buttons for moving conditions between panels
  - API: GET /api/condition-templates, POST /api/loans/{loanId}/conditions/bulk
- **Acceptance Criteria:**
  - Modal displays 150+ pre-configured condition templates
  - Category filter works correctly
  - Search filters by name and description
  - Bulk add creates all conditions in single transaction
  - Current Conditions panel shows selected items
  - "My Lists" section shows user's saved condition sets

### #CP-104 - Filter by Status (Processor View)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - 5 filter pills with dynamic counts
  - Pills: Active [N], Need to Request [N], Requested [N], Send Brw Requests [N], Review Docs [N]
  - Visual highlighting on selected filter
  - API: Counts calculated server-side
- **Acceptance Criteria:**
  - Clicking filter pill filters grid to matching conditions
  - Count badges update in real-time
  - Active filter visually highlighted
  - Clicking same filter again clears filter

### #CP-105 - Search Conditions (Real-time)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - Search textbox in header
  - Placeholder: "Search Conditions"
  - Debounced search (300ms delay)
  - Searches: condition name, description, ID, category
- **Acceptance Criteria:**
  - Search filters grid as user types (after 300ms)
  - Searches across name, description, ID, category fields
  - Clearing search restores full list
  - Works in combination with filter pills

### #CP-106 - Bulk Selection & Actions
- **Type:** Feature
- **Size:** Small (2-3 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - Checkbox on each condition row
  - "Select All" checkbox in header
  - Selection count badge: "N selected"
  - Bulk action buttons (placeholder for future)
- **Acceptance Criteria:**
  - Clicking checkbox selects/deselects condition
  - Select All checks all visible conditions
  - Count badge shows accurate selection count
  - Selection persists when filtering/searching

### #CP-107 - Collapse/Expand Stage Groups
- **Type:** Feature
- **Size:** Small (1-2 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - Expand/collapse arrow on each stage header
  - "Collapse All" button in header
  - localStorage to persist collapsed state
- **Acceptance Criteria:**
  - Clicking stage header toggles expanded/collapsed
  - "Collapse All" collapses all stages
  - State persists across page reloads
  - Smooth animation on expand/collapse

### #CP-108 - Add/Edit Condition Notes (Inline)
- **Type:** Feature
- **Size:** Small (2-3 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - "Add a note" button on each condition row
  - Inline rich text editor (replaces button when clicked)
  - Toolbar: Bold, Italic, Underline, Strikethrough, Bullet List, Numbered List, Link
  - Save/Cancel buttons
  - API: POST /api/conditions/{conditionId}/notes
- **Acceptance Criteria:**
  - Clicking "Add a note" reveals inline editor
  - Editor supports rich text formatting
  - Save creates note with timestamp and author
  - Note appears in "Condition Notes" section of Edit modal
  - Cancel closes editor without saving

### #CP-109 - Set Flag on Condition (Personal)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-100, CP-102
- **Blocks:** None
- **Components:**
  - "Set Flag" button in Edit Condition modal
  - Expandable section with 5 radio buttons: Red, Blue, Yellow, Green, No Flag
  - Info message: "These flags are your personal flags and will not be visible to others"
  - "Apply" button
  - Visual flag indicator on grid row
  - API: PUT /api/conditions/{conditionId}/flag (user-scoped)
- **Acceptance Criteria:**
  - Flag selection opens in Edit Condition modal
  - Selecting flag and clicking Apply saves flag
  - Flag appears as colored indicator on grid row
  - Flag is user-specific (not visible to other users)
  - Clearing flag (No Flag) removes indicator

### #CP-110 - Exception Request Management
- **Type:** Feature
- **Size:** Medium (3-4 hours)
- **Depends On:** CP-100, CP-102
- **Blocks:** None
- **Components:**
  - "Exception Request" accordion in Edit Condition modal
  - Default message: "There currently is not an exception request"
  - "Create Exception" button (when no exception exists)
  - Exception form: reason, supporting documentation
  - Approval workflow (processor creates, underwriter approves/denies)
  - API: POST /api/conditions/{conditionId}/exceptions, PUT /api/exceptions/{exceptionId}/approve
- **Acceptance Criteria:**
  - Processor can create exception request with reason
  - Underwriter sees exception in their queue for approval
  - Approved exception changes condition status
  - Denied exception requires processor action
  - Exception history tracked

### #CP-111 - Condition Dates (Expiration & Follow-Up)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-100, CP-102
- **Blocks:** None
- **Components:**
  - "Dates" accordion in Edit Condition modal
  - Expiration Date date picker (shows "—" when empty)
  - Follow Up Date date picker (shows "—" when empty)
  - Calendar icon buttons to open pickers
  - API: PUT /api/conditions/{conditionId} (includes dates)
- **Acceptance Criteria:**
  - Clicking calendar icon opens date picker
  - Selecting date updates field and saves to API
  - Dates display in readable format (MM/DD/YYYY)
  - Empty dates show "—" placeholder
  - Past due dates highlighted in red

### #CP-112 - Status History Timeline
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-100, CP-102
- **Blocks:** None
- **Components:**
  - "Condition Status Dates" section in Edit Condition modal (always visible, read-only)
  - Table showing all 7 statuses with timestamps
  - Format: "Status Name: MM/DD/YYYY HH:MM AM/PM" or "—" if not reached
  - Statuses: New, Need Brw Request, Requested, Processor to Review, Ready for UW, Cleared, Not Cleared
- **Acceptance Criteria:**
  - Timeline displays all status transitions
  - Each reached status shows exact timestamp
  - Unreached statuses show "—"
  - Read-only (cannot edit historical data)
  - Timeline updates when status changes

### #CP-113 - Update Loan Status with Submission Notes
- **Type:** Feature
- **Size:** Small (2-3 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - "Update Loan Status" button in header
  - Modal: "Submission Details"
  - Rich text editor with placeholder: "Please add any relevant loan notes for the underwriter prior to submission."
  - Info message: "A loan note will only be visible to members of the loan team."
  - "Next Step: Update Loan Status" indicator
  - "Open Byte Loan Status Page" button (integration)
  - API: POST /api/loans/{loanId}/status-update, Integration: Byte API
- **Acceptance Criteria:**
  - Modal opens when "Update Loan Status" clicked
  - Rich text editor supports formatting
  - Notes saved to loan (not condition-specific)
  - Notes visible to all loan team members
  - "Open Byte" button launches external system (disabled until notes saved)

### #CP-114 - Add Documents to Condition (Dual Source)
- **Type:** Feature
- **Size:** Medium (4-5 hours)
- **Depends On:** CP-100
- **Blocks:** None
- **Components:**
  - "Add Docs" button on each condition row
  - Dropdown menu with 2 options:
    1. "Browse and add docs from CLEAR Docs" (integration)
    2. "Upload from your computer" (standard file upload)
  - File upload UI: drag-drop, file type validation, preview
  - CLEAR Docs browser modal (if option 1 selected)
  - API: POST /api/conditions/{conditionId}/documents, Integration: CLEAR Docs API
- **Acceptance Criteria:**
  - Dropdown reveals two source options
  - CLEAR Docs option opens integration modal
  - File upload supports drag-drop and browse
  - Files validated for type and size
  - Documents linked to condition
  - Document count badge updates

### #CP-115 - View Outstanding Document Requests
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-100, CP-102, CP-101
- **Blocks:** None
- **Components:**
  - "Outstanding Document Requests" accordion in Edit Condition modal
  - List view: document type, request date, requested from, status
  - "Add a Doc Request" button (links to #CP-101)
  - Status badges: Pending, Received, Reviewed
- **Acceptance Criteria:**
  - Accordion shows all doc requests for this condition
  - Each request shows type, date, recipient, status
  - Clicking "Add a Doc Request" triggers CP-101 modal
  - Empty state: "No document requests"

### #CP-116 - Create Custom Condition Template
- **Type:** Feature
- **Size:** Small (3 hours)
- **Depends On:** CP-100, CP-103
- **Blocks:** None
- **Components:**
  - "Custom" button in Add Conditions modal (Available Conditions panel)
  - Modal: "Add Custom Condition"
  - Form fields: Name, Description, Category (dropdown), Number (auto-generated), Stage, Class, Type (INT/BRW), Save as Template (checkbox)
  - Additional sections: Set Flag, Document Requests
  - "Cancel" and "Add Condition" buttons
  - API: POST /api/condition-templates (if Save as Template checked)
- **Acceptance Criteria:**
  - Clicking "Custom" opens custom condition form
  - All 20+ categories available in dropdown
  - Condition number auto-generated based on category
  - "Save as Template" checkbox persists condition for future use
  - Custom condition added to Current Conditions panel
  - If saved as template, appears in "My Custom Templates" category

### #CP-117 - Save/Manage "My Lists"
- **Type:** Feature
- **Size:** Small (3 hours)
- **Depends On:** CP-100, CP-103
- **Blocks:** None
- **Components:**
  - "My Lists" section in Add Conditions modal (top of left panel)
  - Pre-populated lists: "FHA Loans", "Frequently Used" (examples)
  - "Add New List" button
  - Save list modal: name, description, selected conditions
  - API: POST /api/users/{userId}/condition-lists, GET /api/users/{userId}/condition-lists
- **Acceptance Criteria:**
  - User can click "Add New List" after selecting conditions
  - Save modal captures list name and description
  - Saved list appears in "My Lists" section
  - Clicking saved list name loads those conditions into Current Conditions panel
  - Lists are user-specific (not shared across team)

### #CP-118 - Real-time Count Badges Update
- **Type:** Feature
- **Size:** Small (2-3 hours)
- **Depends On:** CP-100, CP-104, CP-106
- **Blocks:** None
- **Components:**
  - WebSocket connection or polling mechanism
  - Updates filter pill counts when conditions change
  - Updates selection count badge
  - Updates stage group counts
  - API: WebSocket endpoint or polling GET /api/loans/{loanId}/counts
- **Acceptance Criteria:**
  - Filter pill counts update without page refresh
  - Selection count reflects accurate number
  - Stage group counts update when conditions move
  - Updates visible within 2 seconds of change
  - No page flicker or jarring updates

---

## TIER 3: UNDERWRITER FEATURES (CP-201 to CP-204)

### #CP-201 - Clear Condition (Underwriter)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-200
- **Blocks:** None
- **Components:**
  - "Clear" button/action in underwriter view
  - Status change to "Cleared"
  - Approval notes field
  - Timestamp and underwriter name recorded
  - API: PUT /api/conditions/{conditionId}/clear
- **Acceptance Criteria:**
  - Underwriter can mark condition as "Cleared"
  - Approval notes captured (optional)
  - Timestamp and underwriter recorded in status history
  - Condition moves out of underwriter queue
  - Processor notified of clearance

### #CP-202 - Reject Condition (Underwriter)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-200
- **Blocks:** None
- **Components:**
  - "Reject" or "Not Cleared" action
  - Status change to "Not Cleared"
  - Rejection reason field (required)
  - Sends condition back to processor
  - API: PUT /api/conditions/{conditionId}/reject
- **Acceptance Criteria:**
  - Underwriter can mark condition as "Not Cleared"
  - Rejection reason required (cannot be empty)
  - Condition returns to processor queue
  - Processor notified of rejection with reason
  - Status history records rejection

### #CP-203 - Request Additional Info (UW to Processor)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-200
- **Blocks:** None
- **Components:**
  - "Request Info" button in underwriter view
  - Status change to "Processor to Review"
  - Comments field for underwriter to specify what's needed
  - Notification to processor
  - API: PUT /api/conditions/{conditionId}/request-info
- **Acceptance Criteria:**
  - Underwriter can send condition back for more information
  - Status changes to "Processor to Review"
  - Comments field captures what additional info is needed
  - Processor receives notification with comments
  - Processor can see underwriter's request in condition notes

### #CP-204 - Escalate Condition for Review (Underwriter)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-200
- **Blocks:** None
- **Components:**
  - "Escalate" button for complex conditions
  - Escalation reason field
  - Escalation notification to senior underwriter/manager
  - Condition flagged in system
  - API: POST /api/conditions/{conditionId}/escalate
- **Acceptance Criteria:**
  - Underwriter can escalate difficult conditions
  - Escalation reason captured
  - Senior underwriter/manager notified
  - Condition appears in escalated conditions queue
  - Original underwriter remains assigned

---

## TIER 3: BORROWER FEATURES (CP-301 to CP-304)

### #CP-301 - View Required Documents List (Borrower)
- **Type:** Feature
- **Size:** Small (2 hours)
- **Depends On:** CP-300
- **Blocks:** None
- **Components:**
  - Borrower portal view showing only BRW-type conditions
  - Simplified language (no internal jargon)
  - Document request list with due dates
  - Status indicators: Pending, Submitted, Approved
  - API: GET /api/borrowers/{borrowerId}/document-requests
- **Acceptance Criteria:**
  - Borrower sees only conditions marked Type: "BRW"
  - Language is borrower-friendly (no acronyms)
  - Each document request shows: name, description, due date, status
  - Overdue requests highlighted
  - Mobile-responsive

### #CP-302 - Upload Documents for Condition (Borrower)
- **Type:** Feature
- **Size:** Medium (4-5 hours)
- **Depends On:** CP-300, CP-301
- **Blocks:** None
- **Components:**
  - "Upload Document" button for each request
  - File upload UI: drag-drop, multiple file support
  - File preview before submission
  - Progress indicator during upload
  - Success/error messaging
  - API: POST /api/document-requests/{requestId}/upload
- **Acceptance Criteria:**
  - Borrower can upload files via drag-drop or browse
  - Multiple files supported per request
  - File size limit enforced (10MB per file)
  - Supported formats: PDF, JPG, PNG, DOCX
  - Progress bar shows upload status
  - Success message confirms upload
  - Processor notified of new document

### #CP-303 - Track Condition Status & Timeline (Borrower)
- **Type:** Feature
- **Size:** Small (2-3 hours)
- **Depends On:** CP-300
- **Blocks:** None
- **Components:**
  - Status timeline view: Requested → Submitted → Under Review → Approved/Rejected
  - Visual progress indicator
  - Timestamp for each stage
  - Estimated completion date
  - API: GET /api/borrowers/{borrowerId}/conditions/status
- **Acceptance Criteria:**
  - Borrower sees visual timeline of condition status
  - Current stage highlighted
  - Completed stages show checkmark and timestamp
  - Pending stages grayed out
  - Estimated completion date displayed (if available)

### #CP-304 - Receive Notifications for Updates (Borrower)
- **Type:** Feature
- **Size:** Small (2-3 hours)
- **Depends On:** CP-300
- **Blocks:** None
- **Components:**
  - Email notifications: new document request, document approved, document rejected
  - SMS notifications (opt-in)
  - In-app notification bell icon with count badge
  - Notification preferences page
  - API: POST /api/notifications/send (triggered by events)
- **Acceptance Criteria:**
  - Borrower receives email when document requested
  - Borrower receives email when document approved/rejected
  - SMS opt-in available in preferences
  - In-app bell icon shows unread count
  - Clicking notification navigates to relevant condition

---

## TIER 3: CROSS-CUTTING FEATURES (CP-400 to CP-404)

### #CP-400 - Activity History & Audit Log
- **Type:** Feature
- **Size:** Medium (4 hours)
- **Depends On:** CP-001
- **Blocks:** None
- **Components:**
  - Activity log view showing all actions on condition
  - Filterable by action type, user, date range
  - Audit trail: who, what, when, from/to values
  - Export to CSV
  - API: GET /api/conditions/{conditionId}/audit-log
- **Acceptance Criteria:**
  - All condition changes logged with timestamp and user
  - Log shows before/after values for edited fields
  - Filterable by action type and date
  - Exportable to CSV
  - Log immutable (cannot be edited or deleted)

### #CP-401 - Email & SMS Notifications
- **Type:** Feature
- **Size:** Medium (4-5 hours)
- **Depends On:** CP-001
- **Blocks:** None
- **Components:**
  - Email notification system (SMTP integration)
  - SMS notification system (Twilio/similar)
  - Notification templates: document requested, status changed, condition cleared
  - Notification preferences per user
  - API: POST /api/notifications/send, Integration: SMTP + SMS gateway
- **Acceptance Criteria:**
  - Processor notified when borrower uploads document
  - Underwriter notified when condition ready for review
  - Borrower notified when document requested
  - Borrower notified when condition cleared
  - Users can opt-out of specific notification types
  - Notifications sent within 1 minute of trigger event

### #CP-402 - Export Conditions Report (PDF/Excel)
- **Type:** Feature
- **Size:** Small (2-3 hours)
- **Depends On:** CP-001
- **Blocks:** None
- **Components:**
  - "Export" button in header
  - Format selector: PDF or Excel
  - Report includes: all visible conditions, current filters, metadata
  - PDF: formatted report with logo
  - Excel: spreadsheet with columns matching grid
  - API: GET /api/loans/{loanId}/conditions/export?format=pdf|xlsx
- **Acceptance Criteria:**
  - Export button generates report based on current view
  - PDF formatted with company branding
  - Excel contains all columns from grid
  - Report respects current filters (only exports visible conditions)
  - Download initiates within 3 seconds

### #CP-403 - CLEAR Docs System Integration
- **Type:** Feature
- **Size:** Medium (5-6 hours)
- **Depends On:** CP-001, CP-114
- **Blocks:** None
- **Components:**
  - API integration with CLEAR Docs
  - Document browser modal
  - Document metadata sync
  - Link CLEAR document to condition
  - API: Integration with CLEAR Docs API endpoints
- **Acceptance Criteria:**
  - User can browse CLEAR Docs from within app
  - Selected documents linked to condition
  - Document metadata (name, date, type) synced
  - Documents accessible via link (opens in CLEAR)
  - Integration handles authentication

### #CP-404 - Byte API Integration (Loan Data Sync)
- **Type:** Feature
- **Size:** Medium (5-6 hours)
- **Depends On:** CP-001, CP-113
- **Blocks:** None
- **Components:**
  - API integration with Byte
  - Loan data pull: borrower info, loan amount, property address
  - Condition data push: status updates to Byte
  - "Open Byte Loan Status Page" button functionality
  - API: Integration with Byte API endpoints
- **Acceptance Criteria:**
  - Loan data automatically synced from Byte
  - Condition status changes pushed to Byte
  - "Open Byte" button launches external system with loan context
  - Sync errors handled gracefully with retry logic
  - Integration authenticated via OAuth or API key

---

## DEPENDENCY CHAINS

### Critical Path (Must be sequential):
1. **CP-001** (Platform) → **CP-100** (Processor Shell) → **CP-101 to CP-118** (Processor Features)
2. **CP-001** (Platform) → **CP-200** (Underwriter Shell) → **CP-201 to CP-204** (Underwriter Features)
3. **CP-001** (Platform) → **CP-300** (Borrower Shell) → **CP-301 to CP-304** (Borrower Features)

### Parallel Work Opportunities (Can be developed simultaneously):
- Once CP-100 complete: **CP-101, CP-104, CP-105, CP-106, CP-107, CP-113** can all be developed in parallel
- Once CP-102 complete: **CP-108, CP-109, CP-110, CP-111, CP-112, CP-115** can all be developed in parallel
- Once CP-103 complete: **CP-116, CP-117** can be developed in parallel
- Cross-cutting features (**CP-400 to CP-404**) can be developed anytime after CP-001

### Integration Dependencies:
- **CP-114** depends on **CP-403** (CLEAR Docs integration) for full functionality
- **CP-113** depends on **CP-404** (Byte API integration) for external system launch
- **CP-401** (notifications) integrates with CP-101, CP-113, CP-201, CP-302, CP-304

---

## TICKET SIZE ESTIMATES

- **Small:** 2-3 hours (single component, minimal API)
- **Medium:** 4-6 hours (multiple components or complex API)
- **Large:** 8+ hours (platform foundation, multiple integrations)

## TOTAL SCOPE

- **Platform:** 1 ticket (CP-001)
- **Role Shells:** 3 tickets (CP-100, CP-200, CP-300)
- **Processor Features:** 18 tickets (CP-101 to CP-118)
- **Underwriter Features:** 4 tickets (CP-201 to CP-204)
- **Borrower Features:** 4 tickets (CP-301 to CP-304)
- **Cross-Cutting Features:** 5 tickets (CP-400 to CP-404)

**TOTAL: 35 tickets**

---

## NOTES

- All ticket IDs follow format: CP-[Tier][Sequence]
  - Platform: CP-001 to CP-099
  - Processor: CP-100 (shell), CP-101 to CP-118 (features)
  - Underwriter: CP-200 (shell), CP-201 to CP-204 (features)
  - Borrower: CP-300 (shell), CP-301 to CP-304 (features)
  - Cross-Cutting: CP-400 to CP-404

- Dependencies explicitly listed in "Depends On" and "Blocks" fields
- API endpoints specified for each feature requiring backend
- Integrations (CLEAR Docs, Byte API) called out explicitly
- Acceptance criteria use Given/When/Then format where applicable
