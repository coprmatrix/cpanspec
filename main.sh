increment_version() {
        local delimiter=.;
        local ver=${3:-1};
        local array=($(echo "$1" | tr $delimiter '\n'));
        array[$2]=$((array[$2]+$ver));
        echo $(local IFS=$delimiter ; echo "${array[*]}");
}

ver="$(cat cpanspec/cpanspec | sed -n 's/our[[:space:]]*$VERSION[[:space:]]*=[[:space:]]*'"'"'\(.*\)'"'"'.*/\1/p;')"
ver="$(increment_version $ver 0 1)"
ver="$(increment_version $ver 1 3)"
sed -i "s/.*\(version:\).*/\1 $ver/" *.obsinfo
