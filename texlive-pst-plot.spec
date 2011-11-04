# revision 24390
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-plot
# catalog-date 2011-10-24 23:09:29 +0200
# catalog-license lppl
# catalog-version 1.31
Name:		texlive-pst-plot
Version:	1.31
Release:	1
Summary:	Plot data using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-plot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-plot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-plot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-plot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides plotting of data (typically from external
files), using PSTricks. Plots my be configured using a wide
variety of parameters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-plot/pst-plot.tex
%{_texmfdistdir}/tex/latex/pst-plot/pst-plot.sty
%doc %{_texmfdistdir}/doc/generic/pst-plot/Changes
%doc %{_texmfdistdir}/doc/generic/pst-plot/README
%doc %{_texmfdistdir}/doc/generic/pst-plot/more_docs/README
%doc %{_texmfdistdir}/doc/generic/pst-plot/more_docs/dtk02-1.pdf
%doc %{_texmfdistdir}/doc/generic/pst-plot/more_docs/dtk02-2.pdf
%doc %{_texmfdistdir}/doc/generic/pst-plot/more_docs/tugboat01-4.pdf
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.dat
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-plot/pst-plot97.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-plot/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
