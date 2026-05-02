<h1> HackTheBox Entreprise Activity Tracking </h1>

<h2> Step 1 : Full CSV Data Generator </h2>

1. Log into HTB and go on https://enterprise.hackthebox.com/user-profile/activity 
2. `Inspect` > `Network` 
3. Click filter button `Fetch / XHR`
4. Search to filter by keyword `activity`
5. Scroll down as far down the page you can so `activity?page=<MAX_PAGE>` is loaded 
6. Click on `Preview` and for each network request, copy the full `data` object into `UserData/<FIRSTNAME_LASTNAME>_HTB_Progression` Folder as Json Files <br>

```bash
# Launch command on folder `<FIRSTNAME_LASTNAME>_HTB_Progression` 
$ python3 htb_progression.py <folderName>
```

<h2> Step 2 : CSV Data - Visual Linear Graph </h2>

```bash
# Launch command by addings each CSV file to args
$ python3 htb_graph_generator.py UserData/<FIRSTNAME_LASTNAME>_HTB_Progression/<HTB_USERNAME>_htb_progression.csv
```