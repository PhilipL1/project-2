if [ -z $DATABASE_URI ] || [ -z   $SECRET_KEY ] || [ -z $MYSQL_DATABASE ] || [ -z $MYSQL_ROOT_PASSWORD ]
then 
    echo "one or more of your secrets has not beens set"
    exit 1
fi

sed \
    -e 's,{{DATABASE_URI}},'$DATABASE_URI',g;'\
    -e 's,{{SECRET_KEY}},'$SECRET_KEY',g;'\
    -e 's,{{MYSQL_ROOT_PASSWORD}},'$MYSQL_ROOT_PASSWORD',g;'\
    -e 's,{{MYSQL_DATABASE}},'$MYSQL_DATABASE',g;' secrets.yaml | kubectl apply -f -
    