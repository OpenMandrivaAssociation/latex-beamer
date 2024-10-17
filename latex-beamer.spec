%define rname   beamer
%define rversion 3-24

Name:           latex-%{rname}
Version:        %(echo %rversion |sed -e 's,-,.,g')
Release:        2
Summary:        LaTeX class to produce presentations 
License:        GPL
Group:          Publishing
URL:            https://bitbucket.org/rivanvx/beamer/wiki/Home
Source0:        http://bitbucket.org/rivanvx/beamer/get/version-%{rversion}.tar.bz2
Requires:       texlive-pgf >= 0:1.01
Requires:       texlive-xcolor >= 0:2.00
Requires:       texlive-latex
BuildRequires:  ghostscript
BuildRequires:  texlive-pgf >= 0:1.01
BuildRequires:  texlive-xcolor >= 0:2.00
BuildRequires:  texlive-latex
BuildRequires:	texlive-makeindex texlive-collection-latex texlive
BuildArch:      noarch

%description
The beamer class is a LaTeX class that allows you to create a beamer
presentation. It can also be used to create slides. It behaves similarly
to other packages like Prosper, but has the advantage that it works
together directly with pdflatex, but also with dvips.

Once you have installed the beamer class, the basic steps to create a
beamer presentation are the following:

* Specify beamer as document class instead of article.
* Structure your LaTeX text using \section and \subsection commands.
* Place the text of the individual slides inside \frame commands.
* Run pdflatex on the text (or latex and dvips).

The beamer class has several useful features: You don't need any
external programs to use it other than pdflatex, but it works also with
dvips. You can easily and intuitively create sophisticated overlays.
Finally, you can easily change the whole slide theme or only parts of
it.

%prep
%setup -q -n rivanvx-beamer-cb16a617839f

%build
# FIXME: this doc can't be built without the themes
pushd doc
%__make

%install
mkdir -p %{buildroot}%{_datadir}/texmf/tex/latex/%{rname}
cp -a base %{buildroot}%{_datadir}/texmf/tex/latex/%{rname}

%post
[ -x %{_bindir}/texhash ] && %{_bindir}/env - %{_bindir}/texhash 2> /dev/null || :

%postun
[ -x %{_bindir}/texhash ] && %{_bindir}/env - %{_bindir}/texhash 2> /dev/null || :

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog FILES INSTALL README TODO
%doc doc/beameruserguide.pdf examples solutions
%{_datadir}/texmf/tex/latex/%{rname}


%changelog
* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0:3.10-1mdv2011.0
+ Revision: 602167
- new version

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0:3.07-4mdv2010.0
+ Revision: 436088
- rebuild
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0:3.07-1mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 David Walluck <walluck@mandriva.org> 0:3.07-1mdv2008.0
+ Revision: 22348
- 3.07
- Import latex-beamer



* Mon Sep 04 2006 David Walluck <walluck@mandriva.org> 0:3.06-2mdv2007.0
- rebuild

* Sat Jan 14 2006 David Walluck <walluck@mandriva.org> 0:3.06-1mdk
- 3.06

* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.21-3mdk
- rebuild for new emacs

* Wed Apr 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0:2.21-2mdk
- remove files which conflicts with tetex-latex

* Fri Sep 03 2004 David Walluck <walluck@mandrake.org> 0:2.21-1mdk
- 2.21
- add `BuildRequires: latex-xcolor >= 0:2.00'

* Fri Apr 23 2004 David Walluck <walluck@mandrake.org> 0:2.20-1mdk
- release
