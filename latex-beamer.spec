%define rname           beamer

Summary: 		LaTeX class to produce presentations 
Name: 			latex-%rname
Version: 		3.06
Release: 		%mkrel 2
Epoch:			0
URL:			http://latex-beamer.sourceforge.net/
Source:	 		http://download.sourceforge.net/latex-beamer/%name-%version.tar.bz2
License: 		GPL
Group: 			Publishing
Requires:		latex-pgf >= 0:1.01
Requires:		latex-xcolor >= 0:2.00
Requires: 		tetex-latex
BuildRequires:		latex-pgf >= 0:1.01
BuildRequires:		latex-xcolor >= 0:2.00
BuildRequires:		ghostscript
BuildRequires:		tetex-latex
BuildArch:		noarch
BuildRoot:              %_tmppath/%name-buildroot

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

%package emacs
Summary:		Emacs AUC TeX style for %{name}
Group:			Publishing
Requires:		%{name} = %{epoch}:%{version}-%{release}
Requires:		emacs

%description emacs
Emacs AUC TeX style for %{name}.

%package lyx
Summary:		LyX templates for %{name}
Group:			Publishing
Requires:		%{name} = %{epoch}:%{version}-%{release}
Requires:		lyx

%description lyx
LyX templates for %{name}.

%prep
%setup -q

%build
# FIXME: this doc can't be built without the themes
#pushd doc
#%{__rm} -f doc/%rname.pdf
#latex %{rname}userguide.tex
#latex %{rname}userguide.tex
#pdflatex %{rname}userguide.tex
#%{__rm} -f %{rname}userguide.{aux,dvi,log,out,toc}
#popd

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_datadir}/texmf/tex/latex/%rname
%{__cp} -a base %{buildroot}%{_datadir}/texmf/tex/latex/%rname
%{__mkdir_p} %{buildroot}%{_datadir}/texmf/tex/latex/%rname/emulation
%{__cp} -a emulation/*.sty %{buildroot}%{_datadir}/texmf/tex/latex/%rname/emulation
%{__cp} -a extensions %{buildroot}%{_datadir}/texmf/tex/latex/%rname
%{__cp} -a themes %{buildroot}%{_datadir}/texmf/tex/latex/%rname

%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp
%{__install} -m 644 emacs/*.el %{buildroot}%{_datadir}/emacs/site-lisp
%{__mkdir_p} %{buildroot}%{_sysconfdir}/emacs/site-start.d
%{__cat} > %{buildroot}%{_sysconfdir}/emacs/site-start.d/beamer.el << EOF
(add-to-list 'TeX-style-path '("%{_datadir}/emacs/site-lisp/beamer.el"))
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/lyx/layouts
%{__install} -m 644 lyx/layouts/*.layout %{buildroot}%{_datadir}/lyx/layouts

%clean
%{__rm} -rf %{buildroot}

%post
[ -x %{_bindir}/texhash ] && %{_bindir}/env - %{_bindir}/texhash 2> /dev/null

%postun
[ -x %{_bindir}/texhash ] && %{_bindir}/env - %{_bindir}/texhash 2> /dev/null

%files
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog FILES INSTALL README TODO doc emulation/examples
%doc examples lyx/examples solutions
%{_datadir}/texmf/tex/latex/%rname

%files emacs
%defattr(0644,root,root,0755)
%{_datadir}/emacs/site-lisp/*.el
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/beamer.el

%files lyx
%defattr(0644,root,root,0755)
%{_datadir}/lyx/layouts/*.layout
