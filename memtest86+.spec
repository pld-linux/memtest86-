Summary:	Thorough, stand alone memory test for i386 systems
Summary(pl):	Kompleksowy, niezale©ny od OS tester pamiЙci dla systemСw i386
Summary(pt_BR):	Testador de memСria completo e independente para sistemas i386
Summary(ru_RU):	Тест памяти для x86-архитектуры
Summary(uk_UA):	Тест пам'ят╕ для x86-арх╕тектури
Name:		memtest86+
Version:	1.55
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.memtest.org/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	944b0d4b2058defb000862d7ee3a3b1c
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

%description -l pl
Memtest86 jest ci╠gЁym, samodzielnym testerem pamiЙci dla systemСw
architektury i386. Testy pamiЙci przez BIOS s╠ tylko szybkim
sprawdzeniem i zazwyczaj nie wykrywaj╠ bЁЙdСw znajdywanych przez
memtest86.

%description -l pt_BR
Memtest86 И um testador de memСria independente (no sentido de que nЦo
roda sob um sistema operacional) e completo para sistemas i386.

%description -l ru_RU
Memtest86 -- тщательный и самостоятельный тест памяти для x86-систем.
Он может быть загружен или с жесткого диска при помощи LILO/GRUB, или
с дискеты.

Тест использует алгоритм "движущихся инверсий", доказавший свою
эффективность при обнаружении сбоев памяти. Не обращайте внимания на
"тест" BIOS -- он практически ничего не значит, так как пропустит
много ошибок из тех, которые обнаружит memtest86.

Также может использоваться для создания загрузочной тест-дискеты.

%description -l uk_UA
Memtest86 -- ретельний та самост╕йний тест пам'ят╕ для x86-систем. В╕н
може бути завантажений як з жорсткого диску за допомогою LILO/GRUB,
так ╕ з дискети.

Тест використову╓ алгоритм "рухаючихся ╕нверс╕й", який дов╕в свою
ефективн╕сть при визначенн╕ негаразд╕в ╕з пам'яттю. Не звертайте уваги
на "тест" BIOS -- в╕н практично н╕чого не означа╓, тому що пройде повз
багатьох збо╖в з тих, що знаходить memtest86.

Також може використовуватися для створення завантажувально╖
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
