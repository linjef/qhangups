import os, glob

from PyQt4 import QtCore, QtGui

from qhangups.ui_qhangupssettings import Ui_QHangupsSettings


class QHangupsSettings(QtGui.QDialog, Ui_QHangupsSettings):
    """Settings dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.populate_ui()

    def populate_ui(self):
        """Load settings and populate dialog"""
        settings = QtCore.QSettings()

        lang_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "languages")

        self.languageComboBox.clear()
        self.languageComboBox.addItem(QtCore.QLocale.languageToString(QtCore.QLocale("en").language()), "en")

        for f in glob.glob(os.path.join(lang_path, "*.qm")):
            file_locale = os.path.splitext(os.path.basename(f))[0].split("_")[-1]
            file_lang = QtCore.QLocale.languageToString(QtCore.QLocale(file_locale).language())
            self.languageComboBox.addItem(file_lang, file_locale)

        language = settings.value("language")
        if not language:
            language = QtCore.QLocale.system().name().split("_")[0]

        i = self.languageComboBox.findData(language)
        if i == -1:
            self.languageComboBox.setCurrentIndex(0)
        else:
            self.languageComboBox.setCurrentIndex(i)

    def accept(self):
        """Save settings after clicking on OK button"""
        settings = QtCore.QSettings()
        settings.setValue("language", self.languageComboBox.itemData(self.languageComboBox.currentIndex()))
        QtGui.QDialog.accept(self)