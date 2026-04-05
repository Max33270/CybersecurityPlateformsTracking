<h1> HackTheBox Entreprise Activity Tracking </h1>

1. Log into HTB and go on https://enterprise.hackthebox.com/user-profile/activity 
2. `Inspect` > `Network` 
3. Click filter button `Fetch / XHR`
4. Search to filter by keyword `activity`
5. Scroll down as far down the page you can so `activity?page=<MAX_PAGE>` is loaded 
6. Click on `Preview` and for each network request, copy the full `data` object into `<FIRSTNAME_LASTNAME>_HTB_Progression` Folder as Json Files

Launch command on folder containing Json Files
```
$ python3 htb_progression.py <folderName>
```