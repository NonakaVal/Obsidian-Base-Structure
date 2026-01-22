
This is your new *vault*.

Make a note of something, [[create a link]], or try [the Importer](https://help.obsidian.md/Plugins/Importer)!

When you're ready, delete this note and make the vault your own.


---

# Changes and Proposed usage structure

Base structure for an Obsidian vault containing templates, snippets, note bases, and auxiliary scripts. Designed as a reusable skeleton for personal organization, Zettelkasten, project management, and automations (Python scripts).

This folder already includes a ready-to-use `.obsidian` configuration (plugins, snippets, themes) plus collections of templates / CSS / scripts to speed up the creation of new vaults.


![img|400](https://imgur.com/TTkN4ay.png)


## :LiInfo: :LiArrowBigRight:  [[3 headspaces ACE]]
## :LiFolder: :LiArrowBigRight: [[Base structure]]

---

<br>


# Features

## Note Creation 

- `Ctrl + N` to create a new note -  [QuickAdd](https://github.com/chhoumann/quickadd) plugin ![](https://imgur.com/f6ezubJ.png)

## Templates

````tabs
tab: 📜 Format
```dataview
TABLE without id file.link as "Template"
FROM "X/Templates/Format"
SORT file.name asc
LIMIT 7
```


tab: & Snippets
```dataview
TABLE without id file.link as "Template"
FROM "X/Templates/Snippet"
SORT file.name asc
LIMIT 10
```
````
## Plugins
- **Calendar** – Calendar view integrated with daily notes
- **Callout Manager** – Create and manage callouts without writing CSS
- **Dataview** – Query and organize notes like a database
- **Force note view mode** – Force a default view mode (reading or editing) per note
- **Hotkeys for specific files** – Custom hotkeys to quickly open specific files
- **Iconize** – Add custom icons to files, folders, and links
- **Meta Bind** – Interactive inputs linked directly to frontmatter
- **Outliner** – Outline-style editing with enhanced shortcuts
- **Paste URL into selection** – Automatically convert selected text into a link
- **Periodic Notes** – Create and manage weekly, monthly, and yearly notes
- **QuickAdd** – Fast content capture using commands, templates, and automation
- **Recent Files** – Quickly access recently opened notes
- **Style Settings** – GUI for customizing themes and plugin styles
- **Tabs** – Tab-based file navigation inside Obsidian
- **Simple Banner** – Add visual banners to notes
- **Tag Wrangler** – Rename, merge, and manage tags across the vault
- **Paste Image Rename** – Automatically rename pasted images 
- **Settings Search** – Quickly search and navigate Obsidian settings

## Bases :LiArrowBigRight: [[X.base]]


-  Views
	- Templates
	- Assets
	- Css Snippets from : https://github.com/r-u-s-h-i-k-e-s-h/Obsidian-CSS-Snippets

<center>
  <img src="https://imgur.com/DVkq04P.jpg" width="100%">
</center>


## Hotkeys

![[Hotkeys]]

# Common Issue Fixes

- Plugins not showing: move the `.obsidian` folder into the vault directory and restart Obsidian.
- CSS snippets not applying: Settings → Appearance → CSS snippets → enable the desired snippet.
- Templater not running: confirm the Templates folder path in the plugin settings.
    

## Key Files / Resources

- `.obsidian/` — configuration and installed plugins.
- `Templates/Format/_ base template.md` — base template for new notes.
- `Scripts/organizacao_obsidian/ChanGe-Templates-Folder.py` — script to reorganize templates (read before running).
- `Assets/Dataview/` — ready-to-use queries and dashboards for Dataview.
    



![[Credits & Attribution]]