# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class Import(models.Model):
    _name = 'convert_invoice.convert_invoice'

    name = fields.Char(
        string='Nama Debitur',
        required=True,
    )
    peminjam = fields.Char(
        string='Nama Peminjam',
    )
    bunga_peminjam = fields.Char(
        string='Bunga Peminjam Pertahun',
    )
    jangka_waktu = fields.Char(
        string='Jangka Waktu Pinjaman (Bulan)',
    )
    tgl_pencairan = fields.Date(
        string='Tanggal Pencairan',
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    priode_pinjaman = fields.Date(
        string='Priode Pinjaman',
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    mulai_pembayaran = fields.Integer(
        string='Mulai Pembayaran Pinjaman (Bulan)',
    )
    bulan = fields.Integer(
        string='Bulan',
    )
    periode = fields.Date(
        string='Periode'
    )
    saldo_awal = fields.Float(
        string='Saldo Awal',
    )
    pokok = fields.Float(
        string='Pokok',
    )
    bunga = fields.Float(
        string='Field Label',
    )
    saldo_akhir = fields.Float(
        string='Saldo Akhir',
    )
    status = fields.Char(
        string='Status',
    )
    tanggal = fields.Date(
        string='Tanggal',
        default=lambda self:time.strftime("%Y-%m-%d")
    )
    is_invoce = fields.Boolean(
        string='Is Invoice',
    )
