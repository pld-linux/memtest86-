Summary:	Thorough, stand alone memory test for i386 systems
Summary(pl.UTF-8):   Kompleksowy, niezależny od OS tester pamięci dla systemów i386
Summary(pt_BR.UTF-8):   Testador de memória completo e independente para sistemas i386
Summary(ru.UTF-8):   Тест памяти для x86-архитектуры
Summary(uk.UTF-8):   Тест пам'яті для x86-архітектури
Name:		memtest86+
Version:	1.70
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.memtest.org/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ee447fa46b75cf98538fa60667eb079d
Patch0:		%{name}-i686-ld.patch
URL:		http://www.memtest.org/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Based on the well-known original memtest86 written by Chris Brady,
memtest86+ is a port by some members of the x86-secret team. Our goal
is to provide an up-to-date and completly reliable version of this
software tool aimed at memory failures detection. Memtest86 is
thorough, stand alone memory test for i386 architecture systems. BIOS
based memory tests are only a quick check and often miss failures that
are detected by Memtest86.

%description -l pl.UTF-8
Memtest86 jest ciągłym, samodzielnym testerem pamięci dla systemów
architektury i386. Testy pamięci przez BIOS są tylko szybkim
sprawdzeniem i zazwyczaj nie wykrywają błędów znajdywanych przez
memtest86.

%description -l pt_BR.UTF-8
Memtest86 é um testador de memória independente (no sentido de que não
roda sob um sistema operacional) e completo para sistemas i386.

%description -l ru.UTF-8
Memtest86 -- тщательный и самостоятельный тест памяти для x86-систем.
Он может быть загружен или с жесткого диска при помощи LILO/GRUB, или
с дискеты.

Тест использует алгоритм "движущихся инверсий", доказавший свою
эффективность при обнаружении сбоев памяти. Не обращайте внимания на
"тест" BIOS -- он практически ничего не значит, так как пропустит
много ошибок из тех, которые обнаружит memtest86.

Также может использоваться для создания загрузочной тест-дискеты.

%description -l uk.UTF-8
Memtest86 -- ретельний та самостійний тест пам'яті для x86-систем. Він
може бути завантажений як з жорсткого диску за допомогою LILO/GRUB,
так і з дискети.

Тест використовує алгоритм "рухаючихся інверсій", який довів свою
ефективність при визначенні негараздів із пам'яттю. Не звертайте уваги
на "тест" BIOS -- він практично нічого не означає, тому що пройде повз
багатьох збоїв з тих, що знаходить memtest86.

Також може використовуватися для створення завантажувальної
тест-дискети.

%prep
%setup -q
#%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags} -fomit-frame-pointer -fno-builtin" \
	SHELL=/bin/sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/boot

install memtest.bin $RPM_BUILD_ROOT/boot/memtest86+

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
/boot/memtest86+
