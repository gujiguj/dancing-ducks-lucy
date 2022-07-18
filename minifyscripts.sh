SCRIPT=$1
npx terser -c -m -o app/static/$SCRIPT.min.js -- app/static/$SCRIPT.js
