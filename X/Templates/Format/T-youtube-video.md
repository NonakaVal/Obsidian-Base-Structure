---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
tags: 
summary: <% tp.system.prompt("summary")%>
status: idea
resources:
related:
rank: 
chance: 
---



<%*
// Get all folders
const items = tp.app.vault.getAllLoadedFiles().filter(x => x instanceof tp.obsidian.TFolder);
// Prompt user to select folder
const selectedItem = (await tp.system.suggester((item) => item.path, items)).path;
// Move current file to be in selected folder
if (selectedItem) {
  await tp.file.move(`${selectedItem}/${tp.file.title}`);
}
-%>
