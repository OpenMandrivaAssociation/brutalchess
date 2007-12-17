%define	name	brutalchess
%define	version	0.5.2
%define	release	%mkrel 2
%define	Summary	A 3D chess game inspired by Battle Chess

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
Group:		Games/Puzzles
License:	GPL
URL:		http://brutalchess.sourceforge.net/
Source0:	%{name}-alpha-%{version}-src.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
BuildRequires:	SDL-devel SDL_image-devel X11-devel
BuildRequires:	desktop-file-utils

%description
Brutal Chess features full 3D graphics, an advanced particle
engine, and several different levels of intelligent AI,
inspired by the once popular "Battle Chess" released by
Interplay circa 1988.

%prep
%setup -q

%build
%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Brutal Chess
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;StrategyGame;BoardGame;X-MandrivaLinux-MoreApplications-Games-Strategy;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_gamesbindir}/%{name}
%{_libdir}/md3view
%{_libdir}/objview
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


