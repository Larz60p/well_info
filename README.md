# well_info
## Wyoming USA Oil well completion document extractor

[Completion Report Link](http://wogcc.state.wy.us/legacywogcce.cfm)

### Initial Requsition:

On the bottom right you'll find a link called 'Wells', then click 'By API Number' enter 2521203 - notice you're entering 7 of a total of 10. If you go to the top and click on 'Completions', you'll see the completions I want to download. For this particular well, there are two. There can be anywhere from zero to five (well that's the most I've seen). Usually, there are several digits added to the end of the api#. 

Let's call our main directory Well Data. Within that 'Text Files' (The text records will hold our apis.txt files. It would be nice to be able to keep them until the files were renamed and verified.) and 'logs' (Can we build a final report to show what was downloaded and what failed, if anything?): and within that 'Completion Reports' (the records here and with geology records both need to keep their names because that's how I can link them in my database (Petra) and 'Geology Records'. 

I don't need any html files to be downloaded. There may be a csv file under the geology reports to be downloaded for a core but that won't be often. It should be included in the thought process just in case though. I don't need the data on the completions report page just the pdfs it links to.

This is a work in progress and will initially change daily, slowing as the project matures.
