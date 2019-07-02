@echo off

set protoc=..\3rdParty\protoc-win32\bin\protoc.exe
set Proto2JsonSchema=Proto2JsonSchema.py
set in=proto
set proto_py=proto_py
set json_schema=json_schema
set ginclude=..\3rdParty\protoc-win32\include\google\protobuf
set third_party=..\3rdParty

set base=%~dp0
set protoc=%base%%protoc%
set Proto2JsonSchema=%base%%Proto2JsonSchema%
set in=%base%%in%
set proto_py=%base%%proto_py%
set json_schema=%base%%json_schema%
set ginclude=%base%%ginclude%
set third_party=%base%%third_party%

echo compiling google proto to py
cd "%third_party%"
for /r "%ginclude%" %%f in (*.proto) do (
    echo %%f
    "%protoc%" --proto_path="%ginclude%" --python_out="." "%%f"
)
echo/

echo compiling proto
cd "%in%"
for /r %%f in (*.proto) do (
    echo %%f
    "%protoc%" --proto_path="%ginclude%" --proto_path="%in%" --python_out="%proto_py%" "%%f"
)
echo/

echo generating json schema
set PYTHONPATH=%PYTHONPATH%;%third_party%
"%Proto2JsonSchema%" -o "%json_schema%" -i "%proto_py%" -m AddressBook_pb2 Test.AddressBook
echo/

echo finish
pause

