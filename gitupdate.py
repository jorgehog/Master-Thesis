import sys
raw_file = """COMMIT="FALSE"

if [ "$1" = "" ]
then
    git add gitcommit.sh -A
    git add gitupdate.py -A

    git add ./bibtex/bibtex.bib -A

    git add ./main/jorgenh_thesis.tex -A
    git add ./main/jorgenh_thesis.pdf -A

    __CHAPTERS__
    

    COMMIT="TRUE"
elif [ "$1" = "--update" ]
then
    ARG=""

    cd chapters
    for File in *
    do
	echo "Found chapter: $File"
	ARG="$ARG $File"
    done
    cd ..
  
    python gitupdate.py $ARG
    echo "Script updated."
    exit 0


else
    echo Unrecognized option $1.
fi

if [ "$COMMIT" = "TRUE" ]
then
    echo ""
    echo -n "Commit message: "
    read -e MESSAGE

    git commit -m "$MESSAGE"
    git push -u origin master
fi
"""

infile = open('gitcommit.sh', 'w')

chapter_gitadd_lines = ""

for arg in sys.argv[1:]:
    chapter_gitadd_lines += "git add ./chapters/%s/ch%s.tex\n    " % (arg, arg)

new_file = raw_file.replace("__CHAPTERS__", chapter_gitadd_lines)

infile.write(new_file)
infile.close()
    
