COMMIT="FALSE"

if [ "$1" = "" ]
then
    git add gitcommit.sh -A
    git add gitupdate.py -A

    git add ./main/jorgenh_thesis.tex -A
    git add ./main/jorgenh_thesis.pdf -A

    git add ./chapters/01QM/ch01QM.tex
    git add ./chapters/02TEST/ch02TEST.tex
    

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
