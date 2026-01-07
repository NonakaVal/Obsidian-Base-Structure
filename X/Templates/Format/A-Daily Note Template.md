---
created: <% tp.date.now("YYYY-MM-DD @ HH:mm") %>
tags:
  - calendar/daily
week: '[[<% tp.date.now("YYYY [Week] WW") %>]]'
---

<% tp.date.now("YYYY-MM-DD") %>’s Note

[[<% tp.date.yesterday("YYYY-MM-DD") %>|↶ Previous Day]] | [[<% tp.date.tomorrow("YYYY-MM-DD") %>|Following Day ↷]]

# Daily Mood 

 `INPUT[inlineSelect(option('🙂 – Neutral'), option('😄 – Happy'), option('😐 – Meh'), option('😞 – Sad'), option('😠 – Frustrated'), showcase):daily-mood]`


# Gratitude

_Start your day by writing down what you're grateful for to foster a sense of contentment and appreciation_
- 

- [ ] 

---



# Work Log #inlog

<%tp.file.cursor()%>

---


# Something good
_Recall and note down positive events from my day, no matter how small._

- [ ] 




# Capture #capture



<%*
const folderPath = "Calendar & Review/Daily Notes";
if (!tp.app.vault.getAbstractFileByPathInsensitive(folderPath)) {
  await tp.app.vault.createFolder(folderPath);
}
await tp.file.move(`${folderPath}/${tp.file.title}`);
-%>

