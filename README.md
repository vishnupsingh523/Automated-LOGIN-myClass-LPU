# Automated-LOGIN-myClass-LPU
<img src="https://img.shields.io/badge/made%20with-python-yellowgreen" />
<h2>Description:</h2>
In this repository with the help of selenium and python I have made a program to login into the myclass.in platform for lovelyprofessional university MYCLASS portal.

<h2>Requirements:</h2>
<li>Selenium should be installed</li>
<h4>Install the selenium where you are making your project or to your system using the pip command</h4>
```
pip install selenium

```
<li>Chrome driver should be installed to your system</li>
  
<h4>To install the 'selenium chromedriver' first you have to install chocolatey in your system</h4>
<h4>You can see the installation of chocolatey <a href = "https://chocolatey.org/install">click here</a>.</h4>
<h4>below is the description from here you can easily learn how to install chocalatey</h4>

1- First, ensure that you are using an administrative shell - you can also install as a non-admin, check out Non-Administrative Installation.
2- Install with powershell.exe
3- With PowerShell, you must ensure Get-ExecutionPolicy is not Restricted. We suggest using ```Bypass ``` to bypass the policy to get things installed or ```AllSigned``` for quite a bit more security.
4- Run Get-ExecutionPolicy. If it returns Restricted, then run 
```
Set-ExecutionPolicy AllSigned 
```
or 
```
Set-ExecutionPolicy Bypass -Scope Process
```
5- Now run the following command:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
6- Wait a few seconds for the command to complete.
7- If you don't see any errors, you are ready to use Chocolatey! Type choco or choco -? now, or see Getting Started for usage instructions
