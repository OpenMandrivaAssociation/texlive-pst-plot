# revision 34063
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-plot
# catalog-date 2014-05-16 13:47:09 +0200
# catalog-license lppl
# catalog-version 1.62
Name:		texlive-pst-plot
Version:	1.62
Release:	4
Summary:	Plot data using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-plot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-plot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-plot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides plotting of data (typically from external
files), using PSTricks. Plots may be configured using a wide
variety of parameters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-plot/pst-plot.tex
%{_texmfdistdir}/tex/generic/pst-plot/pst-plot97.tex
%{_texmfdistdir}/tex/latex/pst-plot/pst-plot.sty
%doc %{_texmfdistdir}/doc/generic/pst-plot/Changes
%doc %{_texmfdistdir}/doc/generic/pst-plot/Contents
%doc %{_texmfdistdir}/doc/generic/pst-plot/README
%doc %{_texmfdistdir}/doc/generic/pst-plot/README-doc
%doc %{_texmfdistdir}/doc/generic/pst-plot/dtk02-1.pdf
%doc %{_texmfdistdir}/doc/generic/pst-plot/dtk02-1.tex
%doc %{_texmfdistdir}/doc/generic/pst-plot/dtk02-2.bib
%doc %{_texmfdistdir}/doc/generic/pst-plot/dtk02-2.pdf
%doc %{_texmfdistdir}/doc/generic/pst-plot/dtk02-2.tex
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.dat
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.eps
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.png
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-plot/tugboat01-4.bib
%doc %{_texmfdistdir}/doc/generic/pst-plot/tugboat01-4.pdf
%doc %{_texmfdistdir}/doc/generic/pst-plot/tugboat01-4.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
