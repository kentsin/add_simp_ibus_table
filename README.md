# add_simp_ibus_table

Add simplified Chinese variants to input method tables.

Use unihan Unihan_Variants Unihan_Variants.txt

all filenames hard coded 

download the source tables from github 

use your editor to cut the largest table into a single text table

run this then paste it back into the original source file

   ibus-table-createdb -s cangjie5.txt
   
   sudo chown root.root cangjie5.db
   
   sudo mv cangjie5.db /usr/share/ibus-table/tables/
