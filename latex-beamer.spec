%bcond_with     manual

%define rname   beamer

Name:           latex-%{rname}
Version:        3.07
Release:        %mkrel 3
Epoch:          0
Summary:        LaTeX class to produce presentations 
License:        GPL
Group:          Publishing
URL:            http://latex-beamer.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/latex-beamer/latex-beamer-%{version}.tar.gz
Requires:       latex-pgf >= 0:1.01
Requires:       latex-xcolor >= 0:2.00
Requires:       tetex-latex
BuildRequires:  ghostscript
BuildRequires:  latex-pgf >= 0:1.01
BuildRequires:  latex-xcolor >= 0:2.00
BuildRequires:  tetex-latex
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%setup -q
%{_bindir}/find . -name '.*.jpg' -o -name '*~' | %{_bindir}/xargs -t %{__rm}

%build
# FIXME: this doc can't be built without the themes
%if %with manual
pushd doc
%{__rm} -f doc/%{rname}.pdf
%{_bindir}/latex %{rname}userguide.tex
%{_bindir}/latex %{rname}userguide.tex
%{_bindir}/pdflatex %{rname}userguide.tex
%{__rm} %{rname}userguide.{aux,dvi,log,out,toc}
popd
%endif

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_datadir}/texmf/tex/latex/%{rname}
%{__cp} -a base %{buildroot}%{_datadir}/texmf/tex/latex/%{rname}
%{__mkdir_p} %{buildroot}%{_datadir}/texmf/tex/latex/%{rname}/emulation
%{__cp} -a emulation/*.sty %{buildroot}%{_datadir}/texmf/tex/latex/%{rname}/emulation
%{__cp} -a extensions %{buildroot}%{_datadir}/texmf/tex/latex/%{rname}
%{__cp} -a themes %{buildroot}%{_datadir}/texmf/tex/latex/%{rname}

%clean
%{__rm} -rf %{buildroot}

%post
[ -x %{_bindir}/texhash ] && %{_bindir}/env - %{_bindir}/texhash 2> /dev/null || :

%postun
[ -x %{_bindir}/texhash ] && %{_bindir}/env - %{_bindir}/texhash 2> /dev/null || :

%files
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog FILES INSTALL README TODO doc emulation/examples examples solutions
%{_datadir}/texmf/tex/latex/%{rname}
