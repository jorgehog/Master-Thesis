COMMIT="FALSE"

if [ "$1" = "" ]
then
    git add gitcommit.sh -A
    git add gitupdate.py -A

    git add ./bibtex/bibtex.bib -A

    git add ./main/jorgenh_thesis.tex -A
    git add ./main/jorgenh_thesis.pdf -A

    git add ./chapters/01frontpage/ch01frontpage.tex
    git add ./chapters/02preface/ch02preface.tex
    git add ./chapters/03intro/ch03intro.tex
    git add ./chapters/04QM/ch04QM.tex
    git add ./chapters/05Manybody/ch05Manybody.tex
    
    

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
