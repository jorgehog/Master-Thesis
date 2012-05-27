COMMIT="FALSE"

if [ "$1" = "" ]
then
    git add ./main/jorgenh_thesis.tex -A
    git add ./main/jorgenh_thesis.pdf -A
    git add ./chapters/01QM/ch01QM.tex -A
    COMMIT="TRUE"

else
    echo Unrecognized option $1.
fi

echo trolol
if [ $COMMIT = "TRUE" ]
then
    echo ""
    echo -n "Commit message: "
    read -e MESSAGE

    git commit -m "$MESSAGE"
    git push -u origin master
fi

