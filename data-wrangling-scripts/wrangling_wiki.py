from wrangler import dw
import sys

if(len(sys.argv) < 3):
	sys.exit('Error: Please include an input and output file.  Example python script.py input.csv output.csv')

w = dw.DataWrangler()

# Split data repeatedly on newline  into  rows
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on="\n",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Split data repeatedly on 'tab'
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on="\t",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character="\""))

# Cut  on '"'
w.add(dw.Cut(column=[],
             table=0,
             status="active",
             drop=False,
             result="column",
             update=True,
             insert_position="right",
             row=None,
             on="\"",
             before=None,
             after=None,
             ignore_between=None,
             which=1,
             max=0,
             positions=None))

# Promote row 1  to header
w.add(dw.SetName(column=[],
                 table=0,
                 status="active",
                 drop=True,
                 names=[],
                 header_row=0))

# Set  undefined  name to  index
w.add(dw.SetName(column=["undefined"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["index"],
                 header_row=None))

# Extract from index between 'Contest ' and ','
w.add(dw.Extract(column=["index"],
                 table=0,
                 status="active",
                 drop=False,
                 result="column",
                 update=False,
                 insert_position="right",
                 row=None,
                 on=".*",
                 before=",",
                 after="Contest ",
                 ignore_between=None,
                 which=1,
                 max=1,
                 positions=None))

# Fill extract  with values from above
w.add(dw.Fill(column=["extract"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Delete  rows where song is null
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="song",
                value=None,
                op_str="is null")])))

# Set  extract  name to  year
w.add(dw.SetName(column=["extract"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["year"],
                 header_row=None))


w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

