Name:		brutalchess
Version:	0.5.2
Release:	8
Summary:	A 3D chess game inspired by Battle Chess
Group:		Games/Strategy
License:	GPLv2+
URL:		https://brutalchess.sourceforge.net/
Source0:	%{name}-alpha-%{version}-src.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		brutalchess-0.5.2-fix-FTBFS.patch
Patch1:		brutalchess-0.5.2-gcc4.3.patch
Patch2:		brutalchess-0.5.2-use-own-fonts.patch
Patch3:		brutalchess-0.5.2-gcc4.7.patch
Requires:	fonts-ttf-dejavu
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	desktop-file-utils

%description
Brutal Chess features full 3D graphics, an advanced particle
engine, and several different levels of intelligent AI,
inspired by the once popular "Battle Chess" released by
Interplay circa 1988.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
autoreconf -fi
%configure2_5x	--disable-sdltest \
		--disable-freetypetest \
		--without-x \
		--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make

%install
%makeinstall_std

# we use system default fot via patch2
rm -fr %{buildroot}%{_gamesdatadir}/%{name}/fonts

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Brutal Chess
Comment=A 3D chess game inspired by Battle Chess
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;StrategyGame;BoardGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%files
%doc AUTHORS ChangeLog NEWS README
%{_gamesbindir}/%{name}
%{_libdir}/md3view
%{_libdir}/objview
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.5.2-6mdv2011.0
+ Revision: 635098
- fix build
- rebuild
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-5mdv2011.0
+ Revision: 616863
- the mass rebuild of 2010.0 packages

* Wed May 13 2009 Samuel Verschelde <stormi@mandriva.org> 0.5.2-4mdv2010.0
+ Revision: 375507
- fix Group (fix #49425)
- fix Licence

* Sat Jul 19 2008 Funda Wang <fwang@mandriva.org> 0.5.2-3mdv2009.0
+ Revision: 238792
- use own own fonts
- add patch fix building

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Jan 25 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.5.2-2mdv2007.0
+ Revision: 113073
- move game to strategy section
- fix buildrequires
- new release: 0.5.2
  replace with new cleaned up spec
  icons

  + Lenny Cartier <lenny@mandriva.com>
    - Buildrequires
    - Buildrequires
    - Import brutalchess

* Fri Aug 25 2006 Lenny Cartier <lenny@mandriva.com> 1.2.5-1mdv2007.0
- new

