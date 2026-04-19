const summaryContent = document.getElementById('summaryContent');
const downloadBtn = document.getElementById('downloadBtn');
const sidebarList = document.getElementById('sidebarList');
const sidebarEmpty = document.getElementById('sidebarEmpty');

const meetings = [
  {
    id: 'product-roadmap-sync',
    title: 'Product Roadmap Sync',
    dateTime: 'Apr 18, 2026 at 10:30 AM',
    duration: '45 min',
    participants: ['Aarav Mehta', 'Priya Shah', 'Neha Kapoor', 'Rohan Iyer'],
    discussionPoints: [
      'Reviewed the Google Meet summary flow and agreed the dashboard should open directly into the latest meeting recap.',
      'Confirmed that meeting history needs to behave like saved records rather than chat sessions.',
      'Discussed keeping the existing glassmorphism look while making the content easier to scan for action items.'
    ],
    tasks: [
      { owner: 'Priya Shah', task: 'Prepare final UI copy for the summary sections.' },
      { owner: 'Rohan Iyer', task: 'Connect saved meeting data to the dashboard once the backend endpoint is ready.' },
      { owner: 'Neha Kapoor', task: 'Validate PDF export formatting with two long meeting summaries.' }
    ],
    deadlines: [
      { label: 'UI copy freeze', date: 'Apr 20, 2026' },
      { label: 'Backend data handoff', date: 'Apr 22, 2026' },
      { label: 'PDF QA pass', date: 'Apr 23, 2026' }
    ],
    nextMeeting: 'Apr 24, 2026 at 11:00 AM',
    notes: [
      'Keep the first summary panel focused on title, date, participants, and decisions.',
      'PDF export should include every visible summary field for easy sharing.',
      'Active meeting state should be obvious in the left sidebar.'
    ]
  },
  {
    id: 'engineering-standup',
    title: 'Engineering Standup',
    dateTime: 'Apr 17, 2026 at 9:15 AM',
    duration: '30 min',
    participants: ['Dev Patel', 'Meera Nair', 'Kabir Sethi', 'Anika Rao'],
    discussionPoints: [
      'Reviewed frontend progress and confirmed the separated HTML, CSS, and JS files are now easier to maintain.',
      'Identified that the dashboard needs a summary-first experience instead of a message composer.',
      'Agreed to prioritize responsive behavior before adding backend integrations.'
    ],
    tasks: [
      { owner: 'Dev Patel', task: 'Clean up unused chat code from the dashboard JavaScript.' },
      { owner: 'Meera Nair', task: 'Create sample meeting records for demo and testing.' },
      { owner: 'Kabir Sethi', task: 'Check mobile spacing and sidebar scrolling.' }
    ],
    deadlines: [
      { label: 'Static dashboard ready', date: 'Apr 19, 2026' },
      { label: 'Responsive review', date: 'Apr 21, 2026' }
    ],
    nextMeeting: 'Apr 21, 2026 at 9:15 AM',
    notes: [
      'The old chatbot input is no longer required for this page.',
      'History cards should show enough context to identify a meeting quickly.',
      'Use local sample data until the Google Meet API integration is connected.'
    ]
  },
  {
    id: 'client-feedback-review',
    title: 'Client Feedback Review',
    dateTime: 'Apr 16, 2026 at 4:00 PM',
    duration: '60 min',
    participants: ['Sara Khan', 'Vikram Bose', 'Elena Morris', 'Ishaan Roy'],
    discussionPoints: [
      'Client liked the clean visual direction and asked for faster access to action items.',
      'Team agreed that deadlines should be grouped in a separate section.',
      'Downloadable summaries were marked as essential for sharing after calls.'
    ],
    tasks: [
      { owner: 'Sara Khan', task: 'Share revised dashboard screenshots with the client.' },
      { owner: 'Vikram Bose', task: 'List all fields required in exported meeting summaries.' },
      { owner: 'Ishaan Roy', task: 'Prepare demo data that matches real Google Meet summaries.' }
    ],
    deadlines: [
      { label: 'Screenshot review', date: 'Apr 19, 2026' },
      { label: 'Export field list', date: 'Apr 20, 2026' },
      { label: 'Demo data complete', date: 'Apr 22, 2026' }
    ],
    nextMeeting: 'Apr 25, 2026 at 3:30 PM',
    notes: [
      'Keep action items short and owner-focused.',
      'The summary needs to be readable when projected during review calls.',
      'PDF filenames should include the meeting title.'
    ]
  }
];

let activeMeetingId = meetings[0]?.id || null;

function escapeHTML(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function getActiveMeeting() {
  return meetings.find(meeting => meeting.id === activeMeetingId);
}

function renderSidebar() {
  sidebarList.querySelectorAll('.history-item').forEach(item => item.remove());
  sidebarEmpty.style.display = meetings.length ? 'none' : 'block';

  meetings.forEach(meeting => {
    const item = document.createElement('button');
    item.type = 'button';
    item.className = `history-item${meeting.id === activeMeetingId ? ' active' : ''}`;
    item.innerHTML = `
      <div class="hi-date">${escapeHTML(meeting.title)}</div>
      <div class="hi-time">${escapeHTML(meeting.dateTime)}</div>
      <div class="hi-preview">${escapeHTML(meeting.participants.join(', '))}</div>
    `;
    item.addEventListener('click', () => loadMeeting(meeting.id));
    sidebarList.appendChild(item);
  });
}

function listItems(items) {
  return items.map(item => `<li>${escapeHTML(item)}</li>`).join('');
}

function renderSummary(meeting) {
  if (!meeting) {
    summaryContent.innerHTML = '<p class="sidebar-empty">No meeting summary available.</p>';
    return;
  }

  summaryContent.innerHTML = `
    <div class="summary-hero">
      <div>
        <div class="summary-kicker">Google Meeting Summary</div>
        <h2 class="summary-title">${escapeHTML(meeting.title)}</h2>
      </div>
      <div class="summary-meta">
        <strong>Date & Time</strong><br>
        ${escapeHTML(meeting.dateTime)}<br>
        ${escapeHTML(meeting.duration)}
      </div>
    </div>

    <div class="summary-grid">
      <section class="summary-section">
        <h3>Participants</h3>
        <ul class="participant-list">${listItems(meeting.participants)}</ul>
      </section>

      <section class="summary-section">
        <h3>Next Meeting Date</h3>
        <p>${escapeHTML(meeting.nextMeeting)}</p>
      </section>

      <section class="summary-section full">
        <h3>Key Discussion Points</h3>
        <ul>${listItems(meeting.discussionPoints)}</ul>
      </section>

      <section class="summary-section full">
        <h3>Tasks Assigned</h3>
        <div class="task-list">
          ${meeting.tasks.map(task => `
            <div class="task-card">
              <span class="task-owner">${escapeHTML(task.owner)}</span>
              ${escapeHTML(task.task)}
            </div>
          `).join('')}
        </div>
      </section>

      <section class="summary-section">
        <h3>Deadlines</h3>
        <div class="deadline-list">
          ${meeting.deadlines.map(deadline => `
            <div class="deadline-item">
              <strong>${escapeHTML(deadline.label)}</strong>
              <span>${escapeHTML(deadline.date)}</span>
            </div>
          `).join('')}
        </div>
      </section>

      <section class="summary-section">
        <h3>AI Notes / Action Items</h3>
        <ul>${listItems(meeting.notes)}</ul>
      </section>
    </div>
  `;
}

function loadMeeting(id) {
  activeMeetingId = id;
  renderSidebar();
  renderSummary(getActiveMeeting());
}

function addPdfList(doc, title, items, cursor) {
  doc.setFont('helvetica', 'bold');
  doc.text(title, 18, cursor.y);
  cursor.y += 7;
  doc.setFont('helvetica', 'normal');

  items.forEach(item => {
    const lines = doc.splitTextToSize(`- ${item}`, 174);
    doc.text(lines, 22, cursor.y);
    cursor.y += lines.length * 6 + 2;
    if (cursor.y > 270) {
      doc.addPage();
      cursor.y = 20;
    }
  });

  cursor.y += 5;
}

function downloadSummaryPdf() {
  const meeting = getActiveMeeting();
  if (!meeting) return;

  const jsPDF = window.jspdf?.jsPDF;
  if (!jsPDF) {
    alert('PDF export is still loading. Please try again in a moment.');
    return;
  }

  const doc = new jsPDF();
  const cursor = { y: 20 };

  doc.setFont('helvetica', 'bold');
  doc.setFontSize(18);
  doc.text('MeetMind AI - Meeting Summary', 18, cursor.y);
  cursor.y += 11;

  doc.setFontSize(14);
  doc.text(meeting.title, 18, cursor.y);
  cursor.y += 8;

  doc.setFont('helvetica', 'normal');
  doc.setFontSize(10);
  doc.text(`Date & Time: ${meeting.dateTime}`, 18, cursor.y);
  cursor.y += 6;
  doc.text(`Duration: ${meeting.duration}`, 18, cursor.y);
  cursor.y += 10;

  addPdfList(doc, 'Participants', meeting.participants, cursor);
  addPdfList(doc, 'Key Discussion Points', meeting.discussionPoints, cursor);
  addPdfList(doc, 'Tasks Assigned', meeting.tasks.map(task => `${task.owner}: ${task.task}`), cursor);
  addPdfList(doc, 'Deadlines', meeting.deadlines.map(deadline => `${deadline.label}: ${deadline.date}`), cursor);
  addPdfList(doc, 'Next Meeting Date', [meeting.nextMeeting], cursor);
  addPdfList(doc, 'AI Notes / Action Items', meeting.notes, cursor);

  const fileName = meeting.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  doc.save(`meetmind-${fileName || 'meeting-summary'}.pdf`);
}

downloadBtn.addEventListener('click', downloadSummaryPdf);

renderSidebar();
renderSummary(getActiveMeeting());
